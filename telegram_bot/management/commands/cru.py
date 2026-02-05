from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            username='admin',
            email='admin@localhost.com',
            telegram_id=1,
            password='admin123',


        )

        user.is_active=True
        user.is_superuser=True
        user.is_staff=True
        user.save()


