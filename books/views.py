from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
import random
from . import models 
from django.db.models import Avg
from django.views import generic


#Listview

class BookListView(generic.ListView):
    template_name = 'books/books_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return models.Books.objects.all()

# def book_list_view(request):
#     if request.method == 'GET':
#         books = models.Books.objects.all()
#         context = {
#             'books': books, 
#         }
#         return render(request, template_name='books/books_list.html', context=context)
    
#Detailview

class BookDetailView(generic.DetailView):
    template_name = 'books/book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, *args, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Books, id=book_id)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['average_score'] = book.reviews.aggregate(Avg('mark'))['mark__avg']
        context['reviews'] = book.reviews.all()
        return context

# def book_detail_view(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(models.Books, id=id)
#         average_score = book_id.reviews.aggregate(Avg('mark'))['mark__avg']
#         reviews = book_id.reviews.all()
#         context = {
#             'book_id': book_id,
#             'average_score': average_score,
#             'reviews': reviews,
#         }
#         return render(request, template_name='books/book_detail.html', context=context)

class CurrentTimeView(generic.View):
    def get(self, request):
        now = timezone.localtime(timezone.now())
        return HttpResponse(f"Текущее время: {now.strftime('%H:%M:%S')}")

class RandomNumberView(generic.View):
    def get(self, request):
        number = random.randint(1, 100)
        return HttpResponse(f"Случайное число: {number}")

class AboutMeView(generic.View):
    def get(self, request):
        return HttpResponse(
            "Меня зовут Алия, мне 19 лет. Я учусь в GEEKS, уже 4 месяц на Backend-разработке, "
            "параллельно пишу книгу. Часто зависаю в Call of Duty с сестрой."
        )