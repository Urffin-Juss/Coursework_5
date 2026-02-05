import os
from dotenv import load_dotenv

from django.core.management.base import BaseCommand
from telegram_bot.bot.application import build_application


class Command(BaseCommand):
    help = "Run Telegram bot"

    def handle(self, *args, **options):
        load_dotenv()

        token = os.getenv("BOT_TOKEN")
        if not token:
            raise RuntimeError("BOT_TOKEN is not set")

        app = build_application(token)
        app.run_polling(drop_pending_updates=True)