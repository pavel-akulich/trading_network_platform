from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        user = User.objects.create(
            email='example@example.com',
            first_name='first_name',
            last_name='last_name',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('password123')
        user.save()
