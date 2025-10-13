from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models, forms

def register_view(request):
    if request.method == 'POST':
        form = forms.CustomUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = forms.CustomUserRegisterForm()
    return render(request, template_name='users/register.html',
                  context={'form': form})

def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('profile')
    else:
        form = forms.AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('users:login')


def profile_view(request):
    if request.method == 'GET':
        users = User.objects.all().order_by('-id')
        return render(request, template_name='users/profile.html',
                      context={
                          'users': users
                      })