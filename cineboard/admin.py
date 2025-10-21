from django.contrib import admin
from . import models

admin.site.register(models.Rating)
admin.site.register(models.Tag)
admin.site.register(models.Movies)
admin.site.register(models.Comments)