from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import generic
from django.db.models import Avg
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from . import models, forms



class CreateMovieView(generic.CreateView):
    model = models.Movies
    form_class = forms.MoviesForm
    template_name = 'cineboard/create_movie.html'
    success_url = '/all_movies/'


class UpdateMovieView(generic.UpdateView):
  form_class = forms.MoviesForm
  template_name = 'cineboard/update_movie.html'
  success_url = '/all_movies/'

  def get_object(self, *args, **kwargs):
    movie_id = self.kwargs.get('id')
    return get_object_or_404(models.Movies, id=movie_id)
  
  def form_valid(self, form):
    print(form.cleaned_data)
    return super(UpdateMovieView, self).form_valid(form=form)


class DeleteMovieView(generic.DeleteView):
  template_name = 'cineboard/delete_movie.html'
  success_url = '/all_movies/'

  def get_object(self, *args, **kwargs):
    movie_id = self.kwargs.get('id')
    return get_object_or_404(models.Movies, id=movie_id)


class RegisterView(generic.View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, template_name='cineboard/register.html',
                      context={'form':form})
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        return render(request, template_name='cineboard/register.html',
                      context={'form': form})
    

class AuthLoginView(generic.View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, template_name='cineboard/login.html', 
                      context={'form':form})
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('cineboard:all_movies')
        return render(request, template_name='cineboard/login.html', 
                      context={'form':form})


class AllMoviesListView(LoginRequiredMixin, generic.ListView):
    model = models.Movies
    template_name = 'cineboard/movie_list.html'
    context_object_name = 'movie_lst'

    def get_queryset(self):
        return models.Movies.objects.all()


class MovieDetailView(generic.DetailView):
    template_name = 'cineboard/movie_detail.html'
    context_object_name = 'movie'

    def get_object(self, *args, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(models.Movies, id=movie_id)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.get_object()
        context['average_score'] = movie.reviews.aggregate(Avg('mark'))['mark__avg']
        context['reviews'] = movie.reviews.all()
        return context

class AuthLogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect('cineboard:login')