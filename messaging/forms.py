from django.forms import ModelForm, CharField, PasswordInput
from messaging.models import *


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        exclude = ('date',
                   'groups', 'user_permissions', 'last_login', 'is_superuser',
                   'is_staff', 'friends', 'is_active', 'date_joined'
                   )


class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ('date', 'id', 'sender',)


class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = ('id',)
