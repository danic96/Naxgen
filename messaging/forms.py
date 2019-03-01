from django.forms import ModelForm, CharField, PasswordInput
from messaging.models import *
from .models import User
from django.contrib.auth.models import UserManager


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        exclude = ('date',
                   'groups', 'user_permissions', 'last_login', 'is_superuser',
                   'is_staff', 'friends', 'is_active', 'date_joined'
                   )

    def save(self):
        user = User.objects.create_user(username=self.cleaned_data['username'],
                                        password=self.cleaned_data['password'],
                                        email=self.cleaned_data['email'],
                                        )
        return user


class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ('date', 'id', 'sender',)


class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = ('id',)
