from telegram import Update
from telegram.ext import ContextTypes

from telegram_bot.bot.keyboards import main_menu_keyboard
from telegram_bot.bot.services.users import get_or_create_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_user = update.effective_user
    if not tg_user:
        return

    user = get_or_create_user(
        telegram_id=tg_user.id,
        username=tg_user.username,
    )

    await update.message.reply_text(
        f"Привет, {tg_user.first_name or 'друг'} 👋",
        reply_markup=main_menu_keyboard()
    )