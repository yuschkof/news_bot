from aiogram import Router
from aiogram.filters import Command
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Стартапы",
        callback_data="news_startups")
    )
    builder.add(types.InlineKeyboardButton(
        text="Бизнес",
        callback_data="news_venture")
    )
    builder.add(types.InlineKeyboardButton(
        text="Безопасность",
        callback_data="news_security")
    )
    builder.add(types.InlineKeyboardButton(
        text="Искусственный интеллект",
        callback_data="news_artificial-intelligence")
    )
    builder.add(types.InlineKeyboardButton(
        text="Криптовалюты",
        callback_data="news_cryptocurrency")
    )
    builder.add(types.InlineKeyboardButton(
        text="Приложения",
        callback_data="news_apps")
    )
    builder.adjust(1)
    await message.answer("Чтобы получить новости, выберите категорию", reply_markup=builder.as_markup())