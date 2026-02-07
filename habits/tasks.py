import logging
from datetime import timezone

import os

from anyio import current_time
from celery import shared_task
from django.contrib.sites import requests
from .models import Habit

logger = logging.getLogger(__name__)



@shared_task
def send_habit_reminder():

    logger.info("Sending reminder")

    now = timezone.now()
    current_time = now.time()
    current_date = now.date()

    habits = Habit.objects.filter(is_published=False)

    for habit in habits:

       if habit.time == current_time:


           params = {

               'message': f'Time to use {habit.action}',
               'telegram_id': habit.user.telegram_id,


           }


           response = requests.get(f'{os.getenv('TELEGRAM_API_URL')}{os.getenv('TELEGRAM_BOT_TOKEN')}/sendMessage',
                                   params=params)







