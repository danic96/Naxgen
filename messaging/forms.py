from django.forms import ModelForm
from messaging.models import *


class UserForm(ModelForm):
    class Meta:
        model = User
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
