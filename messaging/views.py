from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import loader, Context
from django.views.generic import DetailView
from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView

from messaging.forms import *
from messaging.models import *
from .forms import UserForm
from django.db.models import Q

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


class GroupUpdate(UpdateView):
    model = Group
    fields = ['members']
    template_name = 'messaging/form.html'

    def form_valid(self, form):
        form.instance.sender = self.request.user
        for user in form.cleaned_data['members']:
            if self.object not in user.groups.all():
                user.groups.add(self.object)

        #TEMPORAL FIX
        for user in User.objects.filter(group=self.object):
            if user not in form.cleaned_data['members']:
                user.groups.remove(self.object)
        return super(GroupUpdate, self).form_valid(form)


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


def send_reply(request, pk):
    message = Message.objects.get(pk=pk)

    text = request.POST['message']
    to = message.sender
    sender = request.user
    new_message = Message(sender=sender, to=to, text=text)
    new_message.save()

    # return redirect('messaging:message_detail', pk)
    return HttpResponseRedirect(reverse('messaging:message_detail',
                                        args=(pk,)))

def change_friend(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.remove_friend(request.user, friend)
    return redirect('messaging:message_list')


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'messaging/profile.html', args)


def search(request):
    filter_string = request.POST['search']
    if filter_string is not None:
        results = User.objects.filter(Q(username__contains=filter_string) | Q(first_name__contains=filter_string)
                                    | Q(last_name__contains=filter_string) | Q(email__contains=filter_string)
                                    | Q(description__contains=filter_string) | Q(phone__contains=filter_string)
                                    | Q(city__contains=filter_string) | Q(website__contains=filter_string))
        return render(request=request, template_name="messaging/search_users.html", context={'results': results})
    else:
        return redirect('messaging:message_list')
