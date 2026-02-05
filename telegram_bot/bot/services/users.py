from typing import Optional

from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync, sync_to_async
from django.contrib.auth import get_user_model

User = get_user_model()


def _get_or_create_user_sync(telegram_id: int, username: Optional[str]):
    user = User.objects.filter(telegram_id=telegram_id).first()
    if user:
        return user

    base_username = username or f"tg_{telegram_id}"
    unique_username = base_username
    i = 1

    while User.objects.filter(username=unique_username).exists():
        unique_username = f"{base_username}_{i}"
        i += 1

    return User.objects.create_user(
        username=unique_username,
        telegram_id=telegram_id,
    )

get_or_create_user = sync_to_async(_get_or_create_user_sync, thread_sensitive=True)