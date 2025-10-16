from django.urls import path
from . import views

urlpatterns = [
    path('all_clothes/', views.all_clothes, name='all_clothes'),
    path('kids_clothes/', views.kids_clothes, name='kids_clothes'),
    path('men_clothes/', views.men_clothes, name='men_clothes'),
    path('women_clothes/', views.women_clothes, name='women_clothes'),
    path('search/', views.seach_view, name='search'),
]