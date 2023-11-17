import os
import asyncio
from datetime import datetime, time
import pytz
import aiohttp

from dotenv import load_dotenv

from database import sqlite_db as db

load_dotenv()
APP_ID = os.getenv("COURSE_KEY")


def get_current_moscow_time():
    moscow_timezone = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_timezone).time()
    current_time_formatted = current_time.strftime('%H:%M')
    return current_time_formatted

async def run_update_loop():
    print("Обновление курса валют запущено")
    while True:
        await update_exchange_rate()
        await asyncio.sleep(3)
