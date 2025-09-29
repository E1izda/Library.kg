from django.urls import path
from . import views

urlpatterns = [
    path('time/', views.current_time, name='current_time'),
    path('random/', views.random_number, name='random_number'),
    path('about_me/', views.about_me, name='about_me'),
]