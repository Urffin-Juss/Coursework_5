from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("📋 Мои привычки", callback_data="menu:my_habits")],
        [InlineKeyboardButton("➕ Добавить привычку", callback_data="menu:add_habit")],
    ]
    return InlineKeyboardMarkup(keyboard)