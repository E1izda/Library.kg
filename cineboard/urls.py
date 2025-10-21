from django.urls import path
from .import views

app_name='cineboard'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.AuthLoginView.as_view(), name='login'),
    path('logout/', views.AuthLogoutView.as_view(), name='logout'),
    path('all_movies/', views.AllMoviesListView.as_view(), name='all_movies'),
    path('all_movies/<int:id>/update/', views.UpdateMovieView.as_view(), name='update'),
    path('all_movies/<int:id>/delete/', views.DeleteMovieView.as_view(), name='delete'),
    path('movie/<int:id>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('create_movie/', views.CreateMovieView.as_view(), name='create_movie')
]