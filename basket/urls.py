from django.urls import path
from . import views

urlpatterns = [
    path('buy_list', views.CreateBuy.as_view(), name='create_buy'),
    path('buy/', views.BuyListView.as_view(), name='buy_list'),
    path('buy/<int:id>/update/', views.BuyUpdateView.as_view(), name='update_buy'),
    path('buy/<int:id>/delete/', views.DeleteBuy.as_view(), name='delete_buy'),
]
