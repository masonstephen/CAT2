# events/management/commands/create_groups.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from events.models import Event

class Command(BaseCommand):
    help = 'Create user groups and assign permissions'

    def handle(self, *args, **kwargs):
        # Create groups
        admin_group, created = Group.objects.get_or_create(name='Admin')
        user_group, created = Group.objects.get_or_create(name='Regular User')

        # Assign permissions
        admin_perms = Permission.objects.filter(content_type__app_label='events')
        user_perms = Permission.objects.filter(content_type__app_label='events', codename='can_view_event')

        admin_group.permissions.set(admin_perms)
        user_group.permissions.set(user_perms)

        self.stdout.write(self.style.SUCCESS('Successfully created groups and assigned permissions'))
