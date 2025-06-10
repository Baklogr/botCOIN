import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


SNAKE_GAME_URL = "https://baklogr.github.io/botCOIN/coin.html" 


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Відправляє вітальне повідомлення з кнопкою, яка відкриває Web App (гру Змійка).
    """
    user = update.effective_user
    
    keyboard = [
        [InlineKeyboardButton("Грати в Змійку 🐍", web_app=WebAppInfo(url=SNAKE_GAME_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_html(
        f"Вітаю, {user.mention_html()}! Ось тестове повідомлення. "
        "Натисни кнопку нижче, щоб відкрити гру 'Змійка' прямо в Telegram:",
        reply_markup=reply_markup
    )

def main() -> None:
    """Запускає бота."""
    application = Application.builder().token("7198607936:AAEEVANeDag3hDBUgGo5BjKkk1NFFJKiifU").build()

    application.add_handler(CommandHandler("start", start))

    print("Бот запущено. Надішліть /start у Telegram.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()