from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField

GENDER = (
        ('m', 'm'),
        ('f', 'f')
    )


class CustomUserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    captcha = CaptchaField()

    class Meta:
        model = models.CustomUser
        fields = (
            'username', 'email',
            'first_name', 'last_name',
            'phone', 'birth_date',
            'city', 'education',
            'experience', 'about_me',
            'password1', 'password2',
            'gender', 'captcha'
        )


class LoginForm(AuthenticationForm):
    captcha = CaptchaField()
