from telegram import Update
from telegram.ext import ContextTypes

from keyboards import main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command."""

    text = (
        "⚽ *Welcome to F11GPT!*\n\n"
        "Your Football Knowledge Assistant.\n\n"
        "Choose a category below."
    )

    await update.message.reply_text(
        text=text,
        reply_markup=main_menu(),
        parse_mode="Markdown",
    )


async def home(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Return to the main menu."""

    query = update.callback_query
    await query.answer()

    text = (
        "⚽ *F11GPT*\n\n"
        "Select one of the categories below."
    )

    await query.edit_message_text(
        text=text,
        reply_markup=main_menu(),
        parse_mode="Markdown",
    )
