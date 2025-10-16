from django.shortcuts import render
from . import models


def seach_view(request):
    query = request.GET.get('s', '')
    clothes_lst = models.Clothes.objects.filter(titles__icontains=query) if query else models.Clothes.none
    context = {
        'clothes': clothes_lst,
        's': query
    }
    return render(request, template_name='clothes/all_clothes.html', context=context)




def all_clothes(request):
    if request.method == 'GET':
        clothes = models.Clothes.objects.all().order_by('-id')
        return render(request, 'clothes/all_clothes.html', 
                      {'clothes': clothes})



def kids_clothes(request):
    if request.method == 'GET':
        clothes = models.Clothes.objects.filter(tags__name='#Детская одежда').order_by('-id')
        return render(request, 'clothes/kids_clothes.html', 
                      {'clothes': clothes})

def men_clothes(request):
    if request.method == 'GET':
        clothes = models.Clothes.objects.filter(tags__name='#Мужская одежда').order_by('-id')
        return render(request, 'clothes/men_clothes.html', 
                      {'clothes': clothes})
    
def women_clothes(request):
    if request.method == 'GET':
        clothes = models.Clothes.objects.filter(tags__name='#Женская одежда').order_by('-id')
        return render(request, 'clothes/women_clothes.html', 
                      {'clothes': clothes})
    
