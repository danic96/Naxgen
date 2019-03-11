from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView

from messaging.forms import *
from messaging.models import *

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
    # form_class = MessageForm
    form_class = MessageForm

    def get_form_kwargs(self):
        kwargs = super(MessageCreate, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super(MessageCreate, self).form_valid(form)


class GroupCreate(CreateView):
    model = Group
    template_name = 'messaging/form.html'
    form_class = GroupForm

    def get_form_kwargs(self):
        kwargs = super(GroupCreate, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
    
    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super(GroupCreate, self).form_valid(form)


class MessageDetail(DetailView):
    model = Message
    template_name = 'messaging/message_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MessageDetail, self).get_context_data(**kwargs)
        return context


class GroupDetail(DetailView):
    model = Group
    template_name = 'messaging/group_detail.html'

    def get_context_data(self, **kwargs):
        context = super(GroupDetail, self).get_context_data(**kwargs)
        return context


def group_message_create(request, pk):
    group = get_object_or_404(Group, pk=pk)
    message = GroupMessage(
        group_id=group,
        text=request.POST['message'],
        from_user=request.user,)
    message.save()
    group.messages.add(message)
    group.save()
    return HttpResponseRedirect(reverse('messaging:group_detail',
                                args=(group.id,)))


class GroupUpdate(UpdateView):
    model = Group
    fields = ['members']
    template_name = 'messaging/form.html'


def change_friend(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.remove_friend(request.user, friend)
    return redirect('messaging:message_list')
