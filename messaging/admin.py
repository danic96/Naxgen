from django.contrib import admin
from messaging import models

from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.

# admin.site.register(models.Author)
admin.site.register(models.Group)
admin.site.register(models.Message)
admin.site.register(models.GroupMessage)
admin.site.register(models.Friend)


class UserAdmin(admin.ModelAdmin):
    model = User
    filter_horizontal = ('user_permissions', 'groups',)


admin.site.register(User, UserAdmin)
