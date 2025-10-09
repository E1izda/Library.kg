from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms

# CREATE — добавить заказ
def createBuy(request):
    if request.method == 'POST':
        form = forms.BuyedBooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buy_list')
    else:
        form = forms.BuyedBooksForm()
    return render(request, template_name='basket/create_buy.html',
                  context={'form': form})


# READ — список всех заказов
def readBuy(request):
    if request.method == 'GET':
        orders = models.BuyedBooks.objects.all().order_by('-id')
    return render(request, template_name='basket/buy_list.html',
                  context={'orders': orders})


# UPDATE — изменить заказ
def updateBuy(request, id):
    buy_id = get_object_or_404(models.BuyedBooks, id=id)
    if request.method == 'POST':
        form = forms.BuyedBooksForm(request.POST, instance=buy_id)
        if form.is_valid():
            form.save()
            return redirect('buy_list')
    else:
        form = forms.BuyedBooksForm(instance=buy_id)

    return render(request, template_name='basket/update_buy.html',
                  context={
                      'form': form,
                      'buy_id': buy_id,
                  })


# DELETE — удалить заказ
def deleteBuy(request, id):
    buy_id = get_object_or_404(models.BuyedBooks, id=id)
    buy_id.delete()
    return redirect('buy_list')


