from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from locales import placeholder_fa, placeholder_en, errors_fa, errors_en

Email = placeholder_en.Email
Email_fa = placeholder_fa.Email
CurrentPassword = placeholder_en.CurrentPassword
CurrentPassword_fa = placeholder_fa.CurrentPassword
Password = placeholder_en.Password
Password_fa = placeholder_fa.Password
ConfirmPassword = placeholder_en.ConfirmPassword
ConfirmPassword_fa = placeholder_fa.ConfirmPassword
error_password_confirmPassword_not_correct = errors_en.password_confirmPassword_not_correct
error_password_confirmPassword_not_correct_fa = errors_fa.password_confirmPassword_not_correct


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": Email, "class": "form-control"}),
        validators=[
            validators.EmailValidator,
        ])
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": Password, "class": "form-control"}),
    )
    confirmPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": ConfirmPassword, "class": "form-control"}),
    )

    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(),required=True)

    def clean_confirmPassword(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirmPassword')

        if confirm_password == password:
            return password
        else:
            raise ValidationError(error_password_confirmPassword_not_correct)


class RegisterForm_fa(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": Email_fa, "class": "form-control"}),
        validators=[
            validators.EmailValidator,
        ])
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": Password_fa, "class": "form-control"}),
    )
    confirmPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": ConfirmPassword_fa, "class": "form-control"}),
    )

    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(), required=True)

    def clean_confirmPassword(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirmPassword')

        if confirm_password == password:
            return password
        else:
            raise ValidationError(error_password_confirmPassword_not_correct_fa)


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "please enter your email", "class": "form-control"}),
        validators=[
            validators.EmailValidator,
        ]
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": Password, "class": "form-control"}),
    )
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(), required=True)


class LoginForm_fa(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": Email_fa, "class": "form-control"}),
        validators=[
            validators.EmailValidator,
        ]
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": Password_fa, "class": "form-control"}),
    )
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(), required=True)


class ForgetPassForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": Email, "class": "form-control"}),
        validators=[
            validators.EmailValidator,
        ]
    )
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(), required=True)


class ForgetPassForm_fa(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": Email_fa, "class": "form-control"}),
        validators=[
            validators.EmailValidator,
        ]
    )
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(), required=True)


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": Password, "class": "form-control"}),
    )
    confirmPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": ConfirmPassword, "class": "form-control"}),
    )

    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(), required=True)

    def clean_confirmPassword(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirmPassword')

        if confirm_password == password:
            return password
        else:
            raise ValidationError(error_password_confirmPassword_not_correct)


class ResetPasswordForm_fa(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": Password_fa, "class": "form-control"}),
    )
    confirmPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": ConfirmPassword_fa, "class": "form-control"}),
    )

    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(), required=True)

    def clean_confirmPassword(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirmPassword')

        if confirm_password == password:
            return password
        else:
            raise ValidationError(error_password_confirmPassword_not_correct_fa)


class AccountActivationWithEmailForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": Email, "class": "form-control"}),
                             validators=[validators.EmailValidator])
    num1 = forms.CharField(max_length=1, widget=forms.NumberInput(attrs={'min': 0, 'max': 9}))
    num2 = forms.CharField(max_length=1, widget=forms.NumberInput(attrs={'min': 0, 'max': 9}))
    num3 = forms.CharField(max_length=1, widget=forms.NumberInput(attrs={'min': 0, 'max': 9}))
    num4 = forms.CharField(max_length=1, widget=forms.NumberInput(attrs={'min': 0, 'max': 9}))
    num5 = forms.CharField(max_length=1, widget=forms.NumberInput(attrs={'min': 0, 'max': 9}))
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(), required=True)


class AccountActivationWithEmailForm_fa(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": Email_fa, "class": "form-control"}),
                             validators=[validators.EmailValidator])
    num1 = forms.CharField(max_length=1, widget=forms.NumberInput(attrs={'min': 0, 'max': 9}))
    num2 = forms.CharField(max_length=1, widget=forms.NumberInput(attrs={'min': 0, 'max': 9}))
    num3 = forms.CharField(max_length=1, widget=forms.NumberInput(attrs={'min': 0, 'max': 9}))
    num4 = forms.CharField(max_length=1, widget=forms.NumberInput(attrs={'min': 0, 'max': 9}))
    num5 = forms.CharField(max_length=1, widget=forms.NumberInput(attrs={'min': 0, 'max': 9}))
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(), required=True)


class AccountActivationForm(forms.Form):
    num1 = forms.CharField(max_length=1, widget=forms.NumberInput(attrs={'min': 0, 'max': 9}))
    num2 = forms.CharField(max_length=1, widget=forms.NumberInput(attrs={'min': 0, 'max': 9}))
    num3 = forms.CharField(max_length=1, widget=forms.NumberInput(attrs={'min': 0, 'max': 9}))
    num4 = forms.CharField(max_length=1, widget=forms.NumberInput(attrs={'min': 0, 'max': 9}))
    num5 = forms.CharField(max_length=1, widget=forms.NumberInput(attrs={'min': 0, 'max': 9}))
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(), required=True)
