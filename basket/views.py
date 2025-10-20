from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic

# CREATE — добавить заказ

class CreateBuy(generic.CreateView):
    model = models.BuyedBooks
    form_class = forms.BuyedBooksForm
    template_name = 'basket/create_buy.html'
    success_url = '/buy_list/'

# def createBuy(request):
#     if request.method == 'POST':
#         form = forms.BuyedBooksForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('buy_list')
#     else:
#         form = forms.BuyedBooksForm()
#     return render(request, template_name='basket/create_buy.html',
#                   context={'form': form})


# READ — список всех заказов

class BuyListView(generic.ListView):
    model = models.BuyedBooks
    template_name = 'basket/buy_list.html'
    context_object_name = 'orders'
    ordering = ['-id']

# def readBuy(request):
#     if request.method == 'GET':
#         orders = models.BuyedBooks.objects.all().order_by('-id')
#     return render(request, template_name='basket/buy_list.html',
#                   context={'orders': orders})


# UPDATE — изменить заказ

class BuyUpdateView(generic.UpdateView):
    model = models.BuyedBooks
    form_class = forms.BuyedBooksForm
    template_name = 'basket/update_buy.html'
    success_url = '/buy_list/'

    def get_object(self, *args, **kwargs):
        buy_id = self.kwargs.get('id')
        return get_object_or_404(models.BuyedBooks, id=buy_id)

    def from_valid(self, form):
        print(form.cleaned_data)
        return super(BuyUpdateView, self). form_valid(form=form)

# def updateBuy(request, id):
#     buy_id = get_object_or_404(models.BuyedBooks, id=id)
#     if request.method == 'POST':
#         form = forms.BuyedBooksForm(request.POST, instance=buy_id)
#         if form.is_valid():
#             form.save()
#             return redirect('buy_list')
#     else:
#         form = forms.BuyedBooksForm(instance=buy_id)

#     return render(request, template_name='basket/update_buy.html',
#                   context={
#                       'form': form,
#                       'buy_id': buy_id,
#                   })


# DELETE — удалить заказ

class DeleteBuy(generic.DeleteView):
    template_name = 'basket/delete_buy.html'
    success_url = '/buy_list/'

    def get_object(self, *args, **kwags):
        buy_id = self.kwargs.get('id')
        return get_object_or_404(models.BuyedBooks, id=buy_id)
    

# def deleteBuy(request, id):
#     buy_id = get_object_or_404(models.BuyedBooks, id=id)
#     buy_id.delete()
#     return redirect('buy_list')


