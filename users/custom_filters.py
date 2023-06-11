from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name="user_in_groups")
def user_in_groups(user, group_names):
    group_names = (group_names).split(",")

    for group_name in group_names:
        try:
            group = Group.objects.get(name=group_name.strip())
            if group in user.groups.all():
                return True
        except Group.DoesNotExist:
            continue
    return False
