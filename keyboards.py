from telegram import InlineKeyboardButton, InlineKeyboardMarkup


# -----------------------------
# MAIN MENU
# -----------------------------
def main_menu():
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

    return InlineKeyboardMarkup(keyboard)


# -----------------------------
# BACK BUTTON
# -----------------------------
def back_menu():
    keyboard = [
        [InlineKeyboardButton("⬅ Back to Main Menu", callback_data="home")]
    ]

    return InlineKeyboardMarkup(keyboard)


# -----------------------------
# LEGENDS MENU
# -----------------------------
def legends_menu():
    keyboard = [
        [InlineKeyboardButton("🇦🇷 Lionel Messi", callback_data="legend_messi")],
        [InlineKeyboardButton("🇵🇹 Cristiano Ronaldo", callback_data="legend_ronaldo")],
        [InlineKeyboardButton("🇧🇷 Pelé", callback_data="legend_pele")],
        [InlineKeyboardButton("🇦🇷 Diego Maradona", callback_data="legend_maradona")],
        [InlineKeyboardButton("⬅ Back", callback_data="home")],
    ]

    return InlineKeyboardMarkup(keyboard)


# -----------------------------
# COMPETITIONS MENU
# -----------------------------
def competitions_menu():
    keyboard = [
        [InlineKeyboardButton("🌍 FIFA World Cup", callback_data="comp_worldcup")],
        [InlineKeyboardButton("🏆 UEFA Champions League", callback_data="comp_ucl")],
        [InlineKeyboardButton("🏴 Premier League", callback_data="comp_epl")],
        [InlineKeyboardButton("🇪🇸 La Liga", callback_data="comp_laliga")],
        [InlineKeyboardButton("⬅ Back", callback_data="home")],
    ]

    return InlineKeyboardMarkup(keyboard)


# -----------------------------
# RULES MENU
# -----------------------------
def rules_menu():
    keyboard = [
        [InlineKeyboardButton("🚩 Offside", callback_data="rule_offside")],
        [InlineKeyboardButton("✋ Handball", callback_data="rule_handball")],
        [InlineKeyboardButton("🎥 VAR", callback_data="rule_var")],
        [InlineKeyboardButton("⚪ Penalty", callback_data="rule_penalty")],
        [InlineKeyboardButton("⬅ Back", callback_data="home")],
    ]

    return InlineKeyboardMarkup(keyboard)


# -----------------------------
# FORMATIONS MENU
# -----------------------------
def formations_menu():
    keyboard = [
        [InlineKeyboardButton("4-3-3", callback_data="form_433")],
        [InlineKeyboardButton("4-4-2", callback_data="form_442")],
        [InlineKeyboardButton("3-5-2", callback_data="form_352")],
        [InlineKeyboardButton("⬅ Back", callback_data="home")],
    ]

    return InlineKeyboardMarkup(keyboard)


# -----------------------------
# QUIZ MENU
# -----------------------------
def quiz_menu():
    keyboard = [
        [InlineKeyboardButton("🎮 Start Quiz", callback_data="start_quiz")],
        [InlineKeyboardButton("⬅ Back", callback_data="home")],
    ]

    return InlineKeyboardMarkup(keyboard)


# -----------------------------
# ABOUT MENU
# -----------------------------
def about_menu():
    keyboard = [
        [InlineKeyboardButton("🌐 Join Channel", url=)],
        [InlineKeyboardButton("⬅ Back", callback_data="home")],
    ]

    return InlineKeyboardMarkup(keyboard)
