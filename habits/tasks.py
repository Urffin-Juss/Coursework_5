import logging
from datetime import timezone
from celery import shared_task
from .models import Habit
from .services import send_message

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
            send_message(habit.action, habit.user.telegram_id)







