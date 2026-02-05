from telegram.ext import Application, CommandHandler, CallbackQueryHandler

from telegram_bot.bot.handlers.start import start
from telegram_bot.bot.handlers.menu import menu_callback


def build_application(token: str) -> Application:
    app = Application.builder().token(token).build()

    # команды
    app.add_handler(CommandHandler("start", start))

    # кнопки
    app.add_handler(CallbackQueryHandler(menu_callback))

    return app