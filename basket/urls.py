from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createBuy, name='create_buy'),
    path('buy/', views.readBuy, name='buy_list'),
    path('update/<int:id>/', views.updateBuy, name='update_buy'),
    path('delete/<int:id>/', views.deleteBuy, name='delete_buy'),
]