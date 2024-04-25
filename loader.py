from aiogram import Bot, Dispatcher
from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.markdown import hbold
from config import TOKEN
from emoji import emojize

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
router = Router()

start_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=emojize(':bullseye: О проекте :bullseye:'),callback_data='about')],
        [InlineKeyboardButton(text=emojize(':check_mark_button: Выбрать профиль	:check_mark_button:'),callback_data='choose')],
        [InlineKeyboardButton(text=emojize(':red_question_mark: Как работать с асситсентом :red_question_mark:'),callback_data='assistant_help')]
    ]
)