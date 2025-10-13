from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    GENDER = (
        ('m', 'm'),
        ('f', 'f')
    )
    phone = models.CharField(max_length=12, default='+996')
    gender = models.CharField(choices=GENDER, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, blank=True)
    education = models.CharField(max_length=200, blank=True)
    experience = models.TextField(verbose_name='Опыт работы', blank=True, default='Мой опыт работы:')
    about_me = models.TextField(verbose_name='Расскажите о себе', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username