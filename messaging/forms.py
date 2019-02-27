from django.forms import ModelForm
from messaging.models import *


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        exclude = ('date',)


class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ('date', 'id',)


class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = ('id',)
