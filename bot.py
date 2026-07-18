import os

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
)

from handlers import start, button


BOT_TOKEN = os.getenv("BOT_TOKEN")


def main():

    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is missing.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("✅ F11GPT Started Successfully...")

    app.run_polling()


if __name__ == "__main__":
    main()
