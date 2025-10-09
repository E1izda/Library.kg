from django.db import models

class Basket(models.Model):
    name = models.CharField(verbose_name='Название корзины')
    email = models.EmailField(verbose_name='Email пользователя')
    address = models.TextField(verbose_name='Адрес доставки', blank=True)

    def __str__(self):
        return self.name


class BuyedBooks(models.Model):
    buyer_name = models.CharField(verbose_name='Имя покупателя', max_length=100, null=True)
    book = models.ForeignKey('books.Books', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)
    buying_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(verbose_name='Статус заказа', default='В обработке')

    def __str__(self):
        return f'{self.buyer_name} - {self.book}'
    
    class Meta:
        verbose_name = 'купленная книга'
        verbose_name_plural = 'купленные книги'