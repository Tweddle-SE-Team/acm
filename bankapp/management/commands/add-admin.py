from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Add an admin user to the database'

    def handle(self, *args, **options):
        User.objects.filter(email='admin@example.com').delete()
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')