import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.enums import ParseMode

import handlers
from loader import TOKEN
from loader import dp, bot

from handlers import cmd_start

async def main() -> None:

    dp.include_router(handlers.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,stream=sys.stdout)
    asyncio.run(main())
