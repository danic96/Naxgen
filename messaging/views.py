from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from messaging.models import *

from messaging.forms import *

# Create your views here.


class UserCreate(CreateView):
    model = User
    template_name = 'messaging/form.html'
    form_class = UserForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserCreate, self).form_valid(form)



class MessageCreate(CreateView):
    model = Message
    template_name = 'messaging/form.html'
    form_class = MessageForm

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super(MessageCreate, self).form_valid(form)
