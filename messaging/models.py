from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=date.today)
    text = models.TextField()


class Author(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.PROTECT)
    date = models.DateField(default=date.today)
    friends = models.ManyToManyField("self")


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    members = models.ManyToManyField(Author)
