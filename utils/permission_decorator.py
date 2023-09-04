from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse


def permission_checker_authenticated(func):
    def warpper(request: HttpRequest, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('login'))

    return warpper
