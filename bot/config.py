import os

# Получаем ключи из переменных окружения (Render)
config = {
    "openai_api_key": os.getenv("OPENAI_API_KEY"),
    "telegram_token": os.getenv("TELEGRAM_TOKEN")
}
