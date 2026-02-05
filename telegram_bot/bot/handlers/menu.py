from telegram import Update
from telegram.ext import ContextTypes

from telegram_bot.bot.keyboards import main_menu_keyboard


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "menu:my_habits":
        await query.edit_message_text(
            "📋 Мои привычки (позже)",
            reply_markup=main_menu_keyboard()
        )

    elif query.data == "menu:add_habit":
        await query.edit_message_text(
            "➕ Добавление привычки (позже)",
            reply_markup=main_menu_keyboard()
        )

    else:
        await query.edit_message_text(
            "Неизвестная команда",
            reply_markup=main_menu_keyboard()
        )