import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from telegram.ext import ApplicationBuilder, CommandHandler,ContextTypes
from api.models import TelegramUser
from asgiref.sync import sync_to_async

TELEGRAM_TOKEN='7618469952:AAFBTz5hZhCx3hhlAzrvNF65vxiWVmGVisk'


# This is a simple Telegram bot that registers users in a Django model when they start the bot.
# It uses the python-telegram-bot library to handle Telegram interactions and Django ORM to manage user data.
@sync_to_async
def save_telegram_user(user):
    TelegramUser.objects.get_or_create(
        telegram_id=user.id,
        defaults={
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
    )

async def start(update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await save_telegram_user(user)
    await update.message.reply_text(
        f"Hello {user.first_name}! Welcome to the bot."
    )

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    print("Bot is polling...")
    app.run_polling()

if __name__ == '__main__':
    main()
    # This will start the bot and keep it running until you stop it manually