from django.db import models
# from django.contrib.auth.models import User
from datetime import date

from django.contrib.auth.models import AbstractUser
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.utils.timezone import now

# Create your models here.


class User(AbstractUser):
    date = models.DateField(default=date.today)
    friends = models.ManyToManyField("self", blank=True)

    def get_absolute_url(self):
        return reverse('messaging:message_list', kwargs={})


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    # date = models.DateTimeField(default=date.ctime(date.today().strftime('%Y-%m-%d %H:%M:[%S[%f]][%z]')))
    # date = models.DateTimeField(default=date.today())
    date = models.DateTimeField(now())
    text = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sender')
    to = models.ForeignKey(User, on_delete=models.PROTECT, related_name='to')

    def get_absolute_url(self):
        return reverse('messaging:message_list', kwargs={})


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default="")
    members = models.ManyToManyField(User, blank=True)

    def get_absolute_url(self):
        return reverse('messaging:message_list', kwargs={})
