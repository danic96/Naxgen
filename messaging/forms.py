from django.forms import ModelForm, CharField, PasswordInput
from messaging.models import *
from .models import User
from django.contrib.auth.models import UserManager
from django.forms.widgets import *
from django import forms


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
                                        first_name=self.cleaned_data['first_name'],
                                        last_name=self.cleaned_data['last_name'],
                                        )
        return user


class MessageForm(ModelForm):
    def __init__(self, request, *args, **kwargs):
        super(MessageForm, self).__init__(**kwargs)
        user = request.user
        if user:
            self.fields['to'].queryset = User.objects.all().exclude(username=user)

    class Meta:
        model = Message
        fields = ['to', 'text']
        exclude = ('date', 'id', 'sender',)


class GroupForm(ModelForm):
    def __init__(self, request, *args, **kwargs):
        super(GroupForm, self).__init__(**kwargs)
        self.user = User.objects.get(username=request.user)

    class Meta:
        model = Group
        exclude = ('id', 'messages',)

    def save(self):
        group = Group(name=self.cleaned_data['name'],)
        group.save()
        group.members.set(self.cleaned_data['members'])

        for member in self.cleaned_data['members']:
            member.groups.add(group)
            member.save()

        self.user.groups.add(group)
        self.user.save()

        return group

