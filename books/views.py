from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import random

def current_time(request):
    now = timezone.localtime(timezone.now())
    return HttpResponse(f"Текущее время: {now.strftime('%H:%M:%S')}")

def random_number(request):
    number = random.randint(1, 100)
    return HttpResponse(f"Случайное число: {number}")

def about_me(request):
    if request.method == 'GET':
        return HttpResponse("Меня зовут Алия, мне 19 лет. Я учусь в GEEKS, уже 4 месяц на Bakend разработке, паралельно пишу книгу.\n"
"Так же часто зависаю в Call of Duty с сестрой.")
