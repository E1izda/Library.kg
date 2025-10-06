from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='Напишите название книги')
    description = models.TextField(verbose_name='Напишите описание книги')
    image = models.ImageField(upload_to='books/', verbose_name='Выберите изображение книги')
    quantity_page = models.PositiveIntegerField(verbose_name='Количество страниц')
    author = models.CharField(max_length=100, blank=True, verbose_name='Автор книги')
    book_audio = models.URLField(blank=True, null=True, verbose_name='Ссылка на аудиокнигу')
    created_at = models.DateTimeField(auto_now_add=True, null=True) 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'



class Reviews(models.Model):
    choice_book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='reviews')
    mark = models.PositiveIntegerField(verbose_name='Оцените книгу от 1 до 5',
                                        validators=[MaxValueValidator(5), MinValueValidator(1)])
    review_text = models.TextField(verbose_name='Ваше мнение о книге')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_book} - {self.mark}'
    
    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'


class Person(models.Model):
    name = models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'человек'
        verbose_name_plural = 'люди'

class Tour(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'тур'
        verbose_name_plural = 'туры'

class Registration(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.person} - {self.tour}'
    
    class Meta:
        verbose_name = 'регистрация'
        verbose_name_plural = 'регистрации'
