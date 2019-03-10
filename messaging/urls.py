from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView

from messaging import views
from messaging.models import *
from messaging.forms import *
from messaging.views import *
from . import  views


urlpatterns = [
    url(r'^$',
        ListView.as_view(
            queryset=Message.objects.all().order_by('-date'),
            context_object_name='latest_message_list',
            template_name='messaging/message_list.html'),
        name='message_list'),

    # URL FOR SENDING A MESSAGE
    url(r'^message/create/$',
        MessageCreate.as_view(),
        name='message_create'),

    # URL FOR READING MESSAGE
    url(r'^message/(?P<pk>\d+)/$',
        MessageDetail.as_view(),
        name='message_detail'),

    # URL FOR CREATING USER
    url(r'^user/create/$',
        UserCreate.as_view(),
        name='user_create'),

    # URL FOR CREATING A GROUP
    url(r'^group/create/$',
        GroupCreate.as_view(),
        name='group_create'),

    # URL FOR VIEWING GROUP
    url(r'^group/(?P<pk>\d+)/$',
        GroupDetail.as_view(),
        name='group_detail'),

    # URL FOR ADDING OR DELETING USERS
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$',
        views.change_friend,
        name='change_friend'),

    # Create a restaurant  review, ex.: /myrestaurants/restaurants/1/reviews/create/
    url(r'^group/(?P<pk>\d+)/message/create/$',
        group_message_create,
        name='group_message_create'),
]
