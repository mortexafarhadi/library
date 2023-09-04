import random

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View

from account.models import User
from locales import errors_en, errors_fa
from utils.email_service import send_email
from utils.language import get_language_with_status
from utils.session_service import get_session_key, set_session_key
from .forms import LoginForm, RegisterForm, ResetPasswordForm, \
    AccountActivationForm, ForgetPassForm, LoginForm_fa, RegisterForm_fa, ForgetPassForm_fa, \
    ResetPasswordForm_fa, AccountActivationWithEmailForm, \
    AccountActivationWithEmailForm_fa


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('profile'))
        else:
            lang, language = get_language_with_status(request)
            if lang == 'fa':
                login_form = LoginForm_fa()
            else:
                login_form = LoginForm()
            context = {
                'form': login_form,
                'dic': language.login,
                'dic_base': language.base,
                'tempStyle': "contact",
            }
            return render(request, 'account/login.html', context)

    def post(self, request):
        lang, language = get_language_with_status(request)
        if lang == 'fa':
            login_form = LoginForm_fa(request.POST)
        else:
            login_form = LoginForm(request.POST)

        if not login_form.is_valid():
            if lang == 'fa':
                login_form.add_error('email', errors_fa.enter_the_information_correctly)
            else:
                login_form.add_error('email', errors_en.enter_the_information_correctly)
        else:
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is None:
                if lang == 'fa':
                    login_form.add_error('email', errors_fa.the_email_or_password_is_incorrect)
                else:
                    login_form.add_error('email', errors_en.the_email_or_password_is_incorrect)
            else:
                if not user.is_active:
                    if lang == 'fa':
                        login_form.add_error('email', errors_fa.your_account_is_not_active)
                    else:
                        login_form.add_error('email', errors_en.your_account_is_not_active)
                else:
                    is_password_correct = user.check_password(user_pass)
                    if not is_password_correct:
                        if lang == 'fa':
                            login_form.add_error('email', errors_fa.the_email_or_password_is_incorrect)
                        else:
                            login_form.add_error('email', errors_en.the_email_or_password_is_incorrect)
                    else:
                        login(request, user)
                        return redirect(reverse('profile'))

        context = {
            'form': login_form,
            'dic': language.login,
            'dic_base': language.base,
            'tempStyle': "contact",
        }
        return render(request, 'account/login.html', context)


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('profile'))
        else:
            lang, language = get_language_with_status(request)
            if lang == 'fa':
                register_form = RegisterForm_fa()
            else:
                register_form = RegisterForm()
            context = {
                'form': register_form,
                'dic': language.register,
                'dic_base': language.base,
                'tempStyle': "contact"
            }
            return render(request, 'account/register.html', context)

    def post(self, request):
        lang, language = get_language_with_status(request)
        if lang == 'fa':
            register_form = RegisterForm_fa(request.POST)
        else:
            register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                if lang == 'fa':
                    register_form.add_error('email', errors_fa.this_email_has_already_been_registered)
                else:
                    register_form.add_error('email', errors_en.this_email_has_already_been_registered)
            else:
                user_password = register_form.cleaned_data.get('password')
                new_user = User(email=user_email, activeCode=random.randint(10000, 100000),
                                resetPasswordLink=get_random_string(100),
                                is_active=False,
                                username=user_email[:user_email.find('@')])
                new_user.set_password(user_password)
                new_user.save()
                setSessionKey(request, 'email', user_email)
                sendMail('Activation Code', new_user.email, new_user, 'emails/activeAccount.html')
                return redirect(reverse('account-activation'))

        context = {
            'form': register_form,
            'dic': language.register,
            'dic_base': language.base,
            'tempStyle': "contact"
        }
        return render(request, 'account/register.html', context)


class ForgetPasswordView(View):
    def get(self, request):
        lang, language = get_language_with_status(request)
        if lang == 'fa':
            forget_pass_form = ForgetPassForm_fa()
        else:
            forget_pass_form = ForgetPassForm()
        context = {
            'form': forget_pass_form,
            'dic': language.forgotPass,
            'dic_base': language.base,
            'tempStyle': "contact"
        }
        return render(request, 'account/forgetPass.html', context)

    def post(self, request):
        lang, language = get_language_with_status(request)
        if lang == 'fa':
            forget_pass_form = ForgetPassForm_fa(request.POST)
        else:
            forget_pass_form = ForgetPassForm(request.POST)
        if not forget_pass_form.is_valid():
            if lang == 'fa':
                forget_pass_form.add_error('email', errors_fa.enter_the_information_correctly)
            else:
                forget_pass_form.add_error('email', errors_en.enter_the_information_correctly)
        else:
            user_email = forget_pass_form.cleaned_data.get('email')
            user = User.objects.filter(email__iexact=user_email).first()
            if user is None:
                if lang == 'fa':
                    forget_pass_form.add_error('email', errors_fa.user_not_found)
                else:
                    forget_pass_form.add_error('email', errors_en.user_not_found)
            else:
                user.resetPasswordLink = get_random_string(100)
                user.save()
                sendMail('Recovery Password', user.email, user, 'emails/forgetPassword.html')
                return redirect(reverse('home'))

        context = {
            'form': forget_pass_form,
            'dic': language.forgotPass,
            'dic_base': language.base,
            'tempStyle': "contact"
        }
        return render(request, 'account/forgetPass.html', context)


class ResetPasswordView(View):
    def get(self, request, reset_pass_link):
        user: User = User.objects.filter(resetPasswordLink__iexact=reset_pass_link).first()
        if user is None:
            return redirect(reverse('login'))
        else:
            lang, language = get_language_with_status(request)
            if lang == 'fa':
                reset_pass_form = ResetPasswordForm_fa()
            else:
                reset_pass_form = ResetPasswordForm()
            context = {
                'form': reset_pass_form,
                'dic': language.resetPass,
                'dic_base': language.base,
                'tempStyle': "contact"
            }
            return render(request, 'account/resetPassword.html', context)

    def post(self, request, reset_pass_link):
        lang, language = get_language_with_status(request)
        if lang == 'fa':
            reset_pass_form = ResetPasswordForm_fa(request.POST)
        else:
            reset_pass_form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(resetPasswordLink__iexact=reset_pass_link).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse('login'))
            else:
                new_pass = reset_pass_form.cleaned_data.get('password')
                user.set_password(new_pass)
                user.resetPasswordLink = get_random_string(100)
                user.save()
                return redirect(reverse('login'))

        context = {
            'form': reset_pass_form,
            'dic': language.resetPass,
            'dic_base': language.base,
            'tempStyle': "contact"
        }
        return render(request, 'account/resetPassword.html', context)


class AccountActivationView(View):
    def get(self, request):
        lang, language = get_language_with_status(request)
        mode = self.request.GET.get('mode')
        if mode is not None and mode == 'have_code':
            if lang == 'fa':
                account_activation_form = AccountActivationWithEmailForm_fa()
            else:
                account_activation_form = AccountActivationWithEmailForm()
        else:
            account_activation_form = AccountActivationForm()
        context = {
            'form': account_activation_form,
            'dic': language.activeCode,
            'dic_base': language.base,
            'tempStyle': "contact"
        }
        return render(request, 'account/accountActivation.html', context)

    def post(self, request):
        lang, language = get_language_with_status(request)
        mode = self.request.GET.get('mode')
        if mode is not None and mode == 'have_code':
            if lang == 'fa':
                account_activation_form = AccountActivationWithEmailForm_fa(request.POST)
            else:
                account_activation_form = AccountActivationWithEmailForm(request.POST)
        else:
            account_activation_form = AccountActivationForm(request.POST)
        if account_activation_form.is_valid():
            if mode is not None and mode == 'have_code':
                email = account_activation_form.cleaned_data.get('email')
            else:
                email = get_session_key(request, 'email')
            num1 = str(account_activation_form.cleaned_data.get('num1'))
            num2 = str(account_activation_form.cleaned_data.get('num2'))
            num3 = str(account_activation_form.cleaned_data.get('num3'))
            num4 = str(account_activation_form.cleaned_data.get('num4'))
            num5 = str(account_activation_form.cleaned_data.get('num5'))
            active_code = num1 + num2 + num3 + num4 + num5
            user: User = User.objects.filter(email__iexact=email).first()
            if user is not None:
                if user.activeCode == active_code:
                    setSessionKey(request, 'email', '')
                    user.activeCode = random.randint(10000, 100000)
                    user.is_active = True
                    user.save()
                    return redirect(reverse('login'))
                else:
                    if lang == 'fa':
                        account_activation_form.add_error('num1', errors_fa.active_code_is_not_correct)
                    else:
                        account_activation_form.add_error('num1', errors_en.active_code_is_not_correct)
            else:
                if mode is not None and mode == 'have_code':
                    if lang == 'fa':
                        account_activation_form.add_error('email', errors_fa.user_not_found)
                    else:
                        account_activation_form.add_error('email', errors_en.user_not_found)
                else:
                    return redirect(reverse('home'))

        context = {
            'form': account_activation_form,
            'dic': language.activeCode,
            'dic_base': language.base,
            'tempStyle': "contact"
        }
        return render(request, 'account/accountActivation.html', context)


def sendMail(subject, email, user, template):
    send_email(subject, email, {'user': user}, template)


def resendCode(request):
    email = get_session_key(request, 'email')
    user: User = User.objects.filter(email__iexact=email).first()
    if user is not None:
        sendMail('Activation Code', user.email, user, 'emails/activeAccount.html')
        return redirect(reverse('account-activation'))