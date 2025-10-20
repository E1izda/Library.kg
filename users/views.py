from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models, forms
from django.views import generic

# Регистрация пользователя
class RegisterView(generic.View):
    def get(self, request):
        form = forms.CustomUserRegisterForm(request.POST)
        return render(request, template_name='users/register.html', 
                      context={'form': form})

    def post(self, request):
        form = forms.CustomUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        return render(request, template_name='users/register.html', 
                      content={'form': form})


# def register_view(request):
#     if request.method == 'POST':
#         form = forms.CustomUserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/login/')
#     else:
#         form = forms.CustomUserRegisterForm()
#     return render(request, template_name='users/register.html',
#                   context={'form': form})


class LoginView(generic.View):
    def get(self, request):
        form = AuthenticationForm(data=request.POST)
        return render(request, template_name='users/login.html', 
                    context={'form': form})
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user)
            return redirect('profile')
        return render(request, template_name='users/login.html',
                      context={'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = forms.AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             login(request, form.get_user())
#             return redirect('profile')
#     else:
#         form = forms.AuthenticationForm()
#     return render(request, 'users/login.html', {'form': form})

#Выход из сессии(из личного кабинета)
class AuthLogoutView(generic.View):
    def post(self, request):
        logout(request)
        return redirect('users:login')
    

# def logout_view(request):
#     logout(request)
#     return redirect('users:login')


class ProfileView(generic.View):
    def get(self, request):
        users = User.objects.all().order_by('-id')
        return render(request, 'users/profile.html', {'users': users})

# def profile_view(request):
#     if request.method == 'GET':
#         users = User.objects.all().order_by('-id')
#         return render(request, template_name='users/profile.html',
#                       context={
#                           'users': users
#                       })