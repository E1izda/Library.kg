from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Tag(models.Model):
    name = models.CharField(max_length=100, default='Ужастик')



class Movies(models.Model):
    GENRE = (
        ('Триллер', 'Триллер'),
        ('Хорор', 'Хоррор'),
        ('Детектив', 'Детектив')
    )
    title = models.CharField(max_length=100, default='Фильм')
    description = models.TextField(default='Описание фильма00')
    genre = models.CharField(max_length=100, choices=GENRE, default='Триллер')
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    choice_book = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='reviews')
    mark = models.PositiveIntegerField(verbose_name='Оцените фильм от 1 до 5',
                                        validators=[MaxValueValidator(5), MinValueValidator(1)])
    review_text = models.TextField(verbose_name='Ваше мнение о фильме ')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_book} - {self.mark}'
    
    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

class Rating(models.Model):
    MARKS = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ('4', "4"),
        ('5', '5')
    )
    choice_films = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='rating')
    marks = models.CharField(max_length=100, choices=MARKS, default='3', null=True)

