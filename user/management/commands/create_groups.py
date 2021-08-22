# Create groups

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

GROUPS = ['admin_user','teacher_user', 'student_user']

## create the default groups
class Command(BaseCommand):
    print("===========Start creating default groups==========")
    def handle(self, *args, **options):
        for group in GROUPS:
            new_group, created = Group.objects.get_or_create(name=group)
            print(new_group,"-->",created)

        print("===========Default groups created==========")