from django.contrib import admin
from messaging import models

# Register your models here.

admin.site.register(models.Author)
admin.site.register(models.Group)
admin.site.register(models.Message)
