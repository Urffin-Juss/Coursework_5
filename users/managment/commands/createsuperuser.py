from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            username='admin',
            email='im@maxsuns',
            telegram_id=options.get('telegram_id'),


        )
        user.set_password(options.get('password'))
        user.is_active=True
        user.is_superuser=True
        user.save()


