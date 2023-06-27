from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from parsers.headlines_parser import get_headlines
from parsers.news_parser import get_url


router = Router()


@router.callback_query(lambda c: c.data.startswith('news_'))
async def process_callback_button_news(callback_query: CallbackQuery):
    category = callback_query.data.split("news_")[1]
    headlines = get_headlines(category)
    builder_headlines = InlineKeyboardBuilder()
    for headline in headlines:
        builder_headlines.add(types.InlineKeyboardButton(
            text=headline[0],
            callback_data=headline[1])
        )
    builder_headlines.adjust(1)
    await callback_query.message.answer(
        f"Вот новости по категории {category}",
        reply_markup=builder_headlines.as_markup()
    )


@router.callback_query(lambda c: c.data.startswith('https://tinyurl.com/'))
async def process_callback_button_news(callback_query: CallbackQuery):
    data = callback_query.data
    text = get_url(data)
    await callback_query.message.answer(text, parse_mode="HTML")