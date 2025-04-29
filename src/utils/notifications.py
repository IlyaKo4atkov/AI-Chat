import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
import asyncio

env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

async def send_telegram_message(
        text: str,
        parse_mode: str = ParseMode.HTML,
        disable_notification: bool = False
) -> bool:
    """Отправка сообщения в Telegram чат."""
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not bot_token or not chat_id:
        logging.error("Telegram credentials not configured!")
        return False

    try:
        # Новый способ указания параметров по умолчанию
        bot = Bot(
            token=bot_token,
            default=DefaultBotProperties(parse_mode=parse_mode)
        )

        await bot.send_message(
            chat_id=chat_id,
            text=text,
            disable_notification=disable_notification
        )
        return True
    except Exception as e:
        logging.error(f"Telegram notification error: {e}")
        return False
    finally:
        await bot.session.close()
