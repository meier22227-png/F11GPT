import random

# -----------------------------
# FOOTBALL FACTS
# -----------------------------

FOOTBALL_FACTS = [
    "Cristiano Ronaldo is one of the highest goal scorers in football history.",
    "Lionel Messi has won multiple Ballon d'Or awards.",
    "The FIFA World Cup is held every four years.",
    "The first FIFA World Cup took place in Uruguay in 1930.",
    "Brazil has won the FIFA World Cup five times.",
    "A football match lasts 90 minutes plus added time.",
    "Each team has 11 players on the field.",
    "The offside rule was introduced to prevent goal hanging.",
    "The Premier League began in 1992.",
    "Real Madrid has won the UEFA Champions League more than any other club."
]

# -----------------------------
# LEGENDS
# -----------------------------

LEGENDS = {
    "messi":
        "🇦🇷 Lionel Messi\n\n"
        "Position: Forward\n"
        "Country: Argentina\n"
        "World Cup Winner: 2022\n"
        "Widely regarded as one of football's greatest players.",

    "ronaldo":
        "🇵🇹 Cristiano Ronaldo\n\n"
        "Position: Forward\n"
        "Country: Portugal\n"
        "Five-time Ballon d'Or winner.\n"
        "Known for his goalscoring and longevity.",

    "pele":
        "🇧🇷 Pelé\n\n"
        "Three-time FIFA World Cup winner with Brazil.\n"
        "One of the greatest footballers of all time.",

    "maradona":
        "🇦🇷 Diego Maradona\n\n"
        "Led Argentina to the 1986 FIFA World Cup title.\n"
        "Famous for the 'Goal of the Century'."
}

# -----------------------------
# COMPETITIONS
# -----------------------------

COMPETITIONS = {
    "World Cup":
        "🌍 FIFA World Cup\n\n"
        "The biggest international football tournament.\n"
        "Held every four years.",

    "Champions League":
        "🏆 UEFA Champions League\n\n"
        "Europe's premier club competition.",

    "Premier League":
        "🏴 Premier League\n\n"
        "England's top professional football league.",

    "La Liga":
        "🇪🇸 La Liga\n\n"
        "Spain's highest football division."
}

# -----------------------------
# RULES
# -----------------------------

RULES = {
    "Offside":
        "A player is offside if they are nearer to the opponent's goal line than both the ball and the second-last defender when the ball is played to them, unless an exception applies.",

    "Handball":
        "Deliberately handling the ball is usually an offense and may result in a free kick or penalty.",

    "VAR":
        "Video Assistant Referee helps officials review certain match-changing incidents.",

    "Penalty":
        "A penalty kick is awarded for certain fouls committed inside a team's own penalty area."
}

# -----------------------------
# FORMATIONS
# -----------------------------

FORMATIONS = {
    "4-3-3":
        "⚽ 4-3-3\n\n"
        "Strengths:\n"
        "• Attacking football\n"
        "• Wide play\n"
        "• High pressing\n\n"
        "Weakness:\n"
        "Requires energetic midfielders.",

    "4-4-2":
        "⚽ 4-4-2\n\n"
        "Strengths:\n"
        "• Balanced\n"
        "• Easy to defend\n"
        "• Two strikers\n\n"
        "Weakness:\n"
        "Can be outnumbered in midfield.",

    "3-5-2":
        "⚽ 3-5-2\n\n"
        "Strengths:\n"
        "• Midfield dominance\n"
        "• Wing-back flexibility\n\n"
        "Weakness:\n"
        "Needs strong wing-backs."
}

# -----------------------------
# HISTORY
# -----------------------------

HISTORY = [
    "Football originated from games played in England during the 19th century.",
    "FIFA was founded in 1904.",
    "The first Ballon d'Or was awarded in 1956.",
    "The Champions League was originally called the European Cup."
]

# -----------------------------
# QUIZ
# -----------------------------

QUIZ = [
    {
        "question": "Who won the 2022 FIFA World Cup?",
        "options": [
            "Argentina",
            "France",
            "Brazil",
            "Germany"
        ],
        "answer": 0
    },
    {
        "question": "How many players are on the pitch for one team?",
        "options": [
            "9",
            "10",
            "11",
            "12"
        ],
        "answer": 2
    },
    {
        "question": "Which country has won the most FIFA World Cups?",
        "options": [
            "Germany",
            "Brazil",
            "Italy",
            "Argentina"
        ],
        "answer": 1
    }
]

# -----------------------------
# HELPERS
# -----------------------------

def random_fact():
    return random.choice(FOOTBALL_FACTS)


def random_history():
    return random.choice(HISTORY)


def random_quiz():
    return random.choice(QUIZ)
