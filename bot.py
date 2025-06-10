import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Увімкнення логування для відлагодження
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# URL твоєї гри "Змійка"
# ЗАМІНИ ЦЕЙ URL НА РЕАЛЬНУ АДРЕСУ ТВОЄЇ ГРИ
SNAKE_GAME_URL = "http://localhost:8000/snake_game.html" 
# Наприклад: "https://yourusername.github.io/your-repo-name/snake_game.html"
# Або якщо ти використовуєш локальний сервер для тестування (пам'ятай про обмеження):
# SNAKE_GAME_URL = "http://localhost:8000/snake_game.html" 

# Обробник команди /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Відправляє вітальне повідомлення з кнопкою, яка відкриває Web App (гру Змійка).
    """
    user = update.effective_user
    
    # Створення кнопки, яка відкриває Web App
    keyboard = [
        [InlineKeyboardButton("Грати в Змійку 🐍", web_app=WebAppInfo(url=SNAKE_GAME_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_html(
        f"Вітаю, {user.mention_html()}! Ось тестове повідомлення. "
        "Натисни кнопку нижче, щоб відкрити гру 'Змійка' прямо в Telegram:",
        reply_markup=reply_markup
    )

# Основна функція для запуску бота
def main() -> None:
    """Запускає бота."""
    # Заміни 'YOUR_BOT_TOKEN' на токен, який ти отримав від BotFather
    application = Application.builder().token("7198607936:AAEEVANeDag3hDBUgGo5BjKkk1NFFJKiifU").build()

    # Додавання обробника команди /start
    application.add_handler(CommandHandler("start", start))

    # Запуск бота (постійне опитування нових повідомлень)
    print("Бот запущено. Надішліть /start у Telegram.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()