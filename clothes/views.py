from django.shortcuts import render
from . import models
from django.views import generic

# Поиск

class SearchView(generic.View):
    def get(self, request):
        query = request.GET.get('s', '')
        if query:
            clothes_lst = models.Clothes.objects.filter(titles__icontains=query)
        else:
            clothes_lst = models.objects.none
        context = {
         'clothes': clothes_lst,
         's': query
        }
        return render(request, template_name='clothes/all_clothes.html', context=context)

# def seach_view(request):
#     query = request.GET.get('s', '')
#     clothes_lst = models.Clothes.objects.filter(titles__icontains=query) if query else models.Clothes.none
#     context = {
#         'clothes': clothes_lst,
#         's': query
#     }
#     return render(request, template_name='clothes/all_clothes.html', context=context)

# Всe вещи

class AllClothesView(generic.View):
    def get(self, request):
        clothes = models.Clothes.objects.all().order_by('-id')
        return render(request, template_name='clothes/all_clothes.html', 
                      context={'clothes': clothes})



# def all_clothes(request):
#     if request.method == 'GET':
#         clothes = models.Clothes.objects.all().order_by('-id')
#         return render(request, 'clothes/all_clothes.html', 
#                       {'clothes': clothes})

# Детская одежда

class KidsClothesView(generic.View):
    model = models.Clothes
    template_name = 'clothes/kids_clothes.html'
    context_object_name = 'clothes'
    ordering = '-id'

    def get_queryset(self):
        kids_clothes = self.model.objects.filter(tags_name='#Детская одежда')
        return kids_clothes

# def kids_clothes(request):
#     if request.method == 'GET':
#         clothes = models.Clothes.objects.filter(tags__name='#Детская одежда').order_by('-id')
#         return render(request, 'clothes/kids_clothes.html', 
#                       {'clothes': clothes})

# Мужская одежда

class MenClothesView(generic.View):
    model = models.Clothes
    template_name = 'clothes/men_clothes.html'
    context_object_name = 'clothes'
    ordering = '-id'

    def get_queryset(self):
        men_clothes = self.model.objects.filter(tags_name='#Мужская одежда')
        return men_clothes
    
# def men_clothes(request):
#     if request.method == 'GET':
#         clothes = models.Clothes.objects.filter(tags__name='#Мужская одежда').order_by('-id')
#         return render(request, 'clothes/men_clothes.html', 
#                       {'clothes': clothes})
    
#Женская одежда


class WomenClothesView(generic.View):
    model = models.Clothes
    template_name = 'clothes/women_clothes.html'
    context_object_name = 'clothes'
    ordering = '-id'

    def get_queryset(self):
        women_clothes = self.model.objects.filter(tags_name='#Женская одежда')
        return women_clothes
    

# def women_clothes(request):
#     if request.method == 'GET':
#         clothes = models.Clothes.objects.filter(tags__name='#Женская одежда').order_by('-id')
#         return render(request, 'clothes/women_clothes.html', 
#                       {'clothes': clothes})
    
