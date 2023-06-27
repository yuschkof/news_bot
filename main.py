import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import common, news


async def main():
    load_dotenv()
    botApi = os.getenv('BOT_TOKEN')
    bot = Bot(token=botApi)
    dp = Dispatcher()
    logging.basicConfig(level=logging.INFO)

    dp.include_router(common.router)
    dp.include_router(news.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())