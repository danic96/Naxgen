from django.db import models
# from django.contrib.auth.models import User
from datetime import date

from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

"""
class Author(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.PROTECT)
    date = models.DateField(default=date.today)
    friends = models.ManyToManyField("self", blank=True)
"""


class User(AbstractUser):
    date = models.DateField(default=date.today)
    friends = models.ManyToManyField("self", blank=True)

    def get_absolute_url(self):
        return reverse('messaging:message_list',
            kwargs={})


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=date.today)
    text = models.TextField()
    sender = models.OneToOneField(User, on_delete=models.PROTECT, related_name='sender', default=None)
    to = models.OneToOneField(User, on_delete=models.PROTECT, related_name='to', default=None)

    def get_absolute_url(self):
        return reverse('messaging:message_list',
            kwargs={})


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    members = models.ManyToManyField(User)
