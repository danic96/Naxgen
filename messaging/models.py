from django.db import models

from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    date = models.DateTimeField(default=timezone.now)
    friends = models.ManyToManyField("self", blank=True)
    groups = models.ManyToManyField('Group')

    def get_absolute_url(self):
        return reverse('messaging:message_list', kwargs={})


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sender')
    to = models.ForeignKey(User, on_delete=models.PROTECT, related_name='to')

    def get_absolute_url(self):
        return reverse('messaging:message_detail', kwargs={id})


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default="")
    members = models.ManyToManyField(User, blank=True)
    messages = models.ManyToManyField('GroupMessage')

    def get_absolute_url(self):
        return reverse('messaging:message_list', kwargs={})


class GroupMessage(models.Model):
    id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(Group, on_delete=models.PROTECT)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    from_user = models.ForeignKey(User, on_delete=models.PROTECT)


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)
        current_user.friends.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, existing_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(existing_friend)
        current_user.friends.remove(existing_friend)
