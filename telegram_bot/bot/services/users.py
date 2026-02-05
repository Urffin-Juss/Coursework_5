from django.contrib.auth import get_user_model

User = get_user_model()


def get_or_create_user(telegram_id: int, username: str | None):
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