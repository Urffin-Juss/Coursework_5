from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, CallbackContext
import logging
from telegram_bot.bot.handlers.start import start
from telegram_bot.bot.handlers.menu import menu_callback
from telegram import Update


logger = logging.getLogger(__name__)

def build_application(token: str) -> Application:
    app = Application.builder().token(token).build()

    # команды
    app.add_handler(CommandHandler("start", start))


    app.add_error_handler(error_handler)

    # кнопки
    app.add_handler(CallbackQueryHandler(menu_callback))

    return app


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.exception("Exception while handling an update:", exc_info=context.error)