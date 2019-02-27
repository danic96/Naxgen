from django.contrib import admin
from messaging import models

from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.

# admin.site.register(models.Author)
admin.site.register(models.Group)
admin.site.register(models.Message)

admin.site.register(User, UserAdmin)