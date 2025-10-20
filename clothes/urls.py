from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.SearchView.as_view(), name='search'),
    path('all/', views.AllClothesView.as_view(), name='all_clothes'),
    path('kids/', views.KidsClothesView.as_view(), name='kids_clothes'),
    path('men/', views.MenClothesView.as_view(), name='men_clothes'),
    path('women/', views.WomenClothesView.as_view(), name='women_clothes'),
]
