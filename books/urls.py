from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='books_list'),
    path('books/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('time/', views.CurrentTimeView.as_view(), name='current_time'),
    path('random/', views.RandomNumberView.as_view(), name='random_number'),
    path('about/', views.AboutMeView.as_view(), name='about_me'),
]