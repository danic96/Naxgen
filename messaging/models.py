from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.


class Author(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.PROTECT)
    date = models.DateField(default=date.today)
    friends = models.ManyToManyField("self")


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=date.today)
    text = models.TextField()
    sender = models.OneToOneField(Author, on_delete=models.PROTECT, related_name='sender', default=None)
    to = models.OneToOneField(Author, on_delete=models.PROTECT, related_name='to', default=None)


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    members = models.ManyToManyField(Author)
