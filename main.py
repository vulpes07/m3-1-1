import asyncio
import logging
from logging import basicConfig
import about_us, echo, start, help
from bot import bot, dp

async def main():
    logging.basicConfig(level=logging.INFO)

    dp.include_router(start.router)
    dp.include_router(help.router)
    dp.include_router(about_us.router)
    dp.include_router(echo.router)
    


    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())