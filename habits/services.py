import requests
from atomic_habits.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_API_URL


def send_message(action, telegram_id):

    params = {

        'text': f'Time to use {action}',
        'chat_id': telegram_id,

    }

    response = requests.get(f'{TELEGRAM_API_URL}{TELEGRAM_BOT_TOKEN}/sendMessage',
                            params=params)



