from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class AuthorForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    phone = forms.CharField(
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    is_active = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "form-control"}),
    )
