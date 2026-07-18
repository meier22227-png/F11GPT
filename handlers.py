from telegram import Update
from telegram.ext import ContextTypes

from keyboards import (
    main_menu,
    legends_menu,
    competitions_menu,
    rules_menu,
    formations_menu,
    quiz_menu,
)

from football_data import (
    random_fact,
    random_history,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "👋 *Welcome to F11GPT!*\n\n"
        "Your Football Knowledge Assistant.\n\n"
        "Choose an option below.",
        parse_mode="Markdown",
        reply_markup=main_menu(),
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    data = query.data

    if data == "home":

        await query.edit_message_text(
            "⚽ *F11GPT*\n\nChoose an option.",
            parse_mode="Markdown",
            reply_markup=main_menu(),
        )

    elif data == "facts":

        await query.edit_message_text(
            random_fact(),
            reply_markup=main_menu(),
        )

    elif data == "history":

        await query.edit_message_text(
            random_history(),
            reply_markup=main_menu(),
        )

    elif data == "legends":

        await query.edit_message_text(
            "⭐ Choose a Football Legend",
            reply_markup=legends_menu(),
        )

    elif data == "competitions":

        await query.edit_message_text(
            "🏆 Choose a Competition",
            reply_markup=competitions_menu(),
        )

    elif data == "rules":

        await query.edit_message_text(
            "📖 Football Rules",
            reply_markup=rules_menu(),
        )

    elif data == "formations":

        await query.edit_message_text(
            "🎯 Football Formations",
            reply_markup=formations_menu(),
        )

    elif data == "quiz":

        await query.edit_message_text(
            "🧠 Football Quiz",
            reply_markup=quiz_menu(),
        )

    elif data == "daily":

        await query.edit_message_text(
            f"🎁 Daily Fact\n\n{random_fact()}",
            reply_markup=main_menu(),
        )

    elif data == "about":

        await query.edit_message_text(
            "ℹ *F11GPT*\n\n"
            "An educational football assistant.\n\n"
            "No Betting\n"
            "No Gambling\n"
            "Just Football Knowledge.",
            parse_mode="Markdown",
            reply_markup=main_menu(),
        )

    else:

        await query.edit_message_text(
            "Coming Soon...",
            reply_markup=main_menu(),
        )
