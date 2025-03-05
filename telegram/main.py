from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from bot import start_handler, repeat_message, env


def main():
    application = ApplicationBuilder().token(env.bot_token).build()

    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(MessageHandler(filters.TEXT, repeat_message))

    application.run_polling()


if __name__ == "__main__":
    main()
