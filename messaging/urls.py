from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from messaging.models import *
from messaging.forms import *
from messaging.views import *

urlpatterns = [
    url(r'^$',
        ListView.as_view(
            queryset=Message.objects.filter(date__lte=timezone.now()).order_by('-date')[:5],
            context_object_name='latest_message_list',
            template_name='messaging/message_list.html'),
        name='message_list'),

    # URL FOR SENDING A MESSAGE
    url(r'^message/create/$',
        MessageCreate.as_view(),
        name='message_create'),

    # URL FOR CREATING USER
    #url(r'^user/create/$',
    #    AuthorCreate.as_view(),
    #    name='user_create'),
]
