import os

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

UserModel = get_user_model()

ADMIN_ID = os.getenv('ADMIN_ID', None)
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', None)
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', None)


class Command(BaseCommand):

    help = 'Initialize Admin User'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))
        if None not in [ADMIN_ID, ADMIN_PASSWORD, ADMIN_EMAIL]:
            try:
                UserModel.objects.get(username=ADMIN_ID)
            except UserModel.DoesNotExist:
                UserModel.objects.create_superuser(ADMIN_ID, f'{ADMIN_ID}@example.com', ADMIN_PASSWORD)
            self.stdout.write(self.style.SUCCESS('All Done !'))
        else:
            self.stdout.write(self.style.ERROR('Missing Admin information in env vars !'))
