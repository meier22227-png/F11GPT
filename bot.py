# bot.py

import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")


keyboard = [
    [
        InlineKeyboardButton("⚽ Football Facts", callback_data="facts"),
        InlineKeyboardButton("🏆 Competitions", callback_data="competitions"),
    ],
    [
        InlineKeyboardButton("⭐ Legends", callback_data="legends"),
        InlineKeyboardButton("📖 Rules", callback_data="rules"),
    ],
    [
        InlineKeyboardButton("🎯 Formations", callback_data="formations"),
        InlineKeyboardButton("🧠 Quiz", callback_data="quiz"),
    ],
    [
        InlineKeyboardButton("🎁 Daily Fact", callback_data="daily"),
        InlineKeyboardButton("📚 History", callback_data="history"),
    ],
    [
        InlineKeyboardButton("ℹ About", callback_data="about"),
    ],
]

reply_markup = InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to *F11GPT!*\n\n"
        "Your Football Knowledge Assistant.\n\n"
        "Choose a category below.",
        reply_markup=reply_markup,
        parse_mode="Markdown",
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    pages = {
        "facts": "⚽ Football Facts\n\nComing soon...",
        "competitions": "🏆 Competitions\n\nComing soon...",
        "legends": "⭐ Football Legends\n\nComing soon...",
        "rules": "📖 Football Rules\n\nComing soon...",
        "formations": "🎯 Football Formations\n\nComing soon...",
        "quiz": "🧠 Football Quiz\n\nComing soon...",
        "daily": "🎁 Daily Football Fact\n\nComing soon...",
        "history": "📚 Football History\n\nComing soon...",
        "about": (
            "ℹ About F11GPT\n\n"
            "An educational football assistant.\n"
            "No betting.\n"
            "No gambling.\n"
            "Just football knowledge."
        ),
    }

    await query.edit_message_text(
        pages.get(query.data, "Unknown option."),
        reply_markup=reply_markup,
    )


def main():
    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN environment variable is not set."
        )

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("F11GPT Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
