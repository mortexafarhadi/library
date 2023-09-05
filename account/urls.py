from django.urls import path

from account import views

urlpatterns = [
    path("register", views.RegisterView.as_view(), name="register"),
    path("login", views.LoginView.as_view(), name="login"),
    path('forget-pass', views.ForgetPasswordView.as_view(), name='forget-pass'),
    path('reset-pass/<reset_pass_link>', views.ResetPasswordView.as_view(), name='reset-pass'),
    path('account-activation', views.AccountActivationView.as_view(), name='account-activation'),
    path("resendCode", views.resendCode, name="resend-code"),
]
