from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            login='admin',
            username='admin',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('9184')
        user.save()