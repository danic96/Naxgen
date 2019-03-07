from .models import Group, GroupMessage


def groups(request):
    return {
        'groups': Group.objects.all()
    }


def group_messages(request):
    return {
        'group_messages': GroupMessage.objects.filter()
    }
