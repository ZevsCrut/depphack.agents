from loader import bot, TOKEN,dp,router

import os
from aiogram import types
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.utils.markdown import hbold
from aiogram.types import FSInputFile
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardRemove
from aiogram import F

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


import loader

class States(StatesGroup):
    Start = State()
    Profile_1 = State()
    Profile_2 = State()
    Profile_3 = State()


@router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext) -> None:
    try:
        await state.clear
    except:
        pass
    logo = types.FSInputFile('start_logo.png')
    await bot.send_photo(chat_id=message.chat.id, photo=logo,
                         caption=loader.text1,
                         reply_markup=loader.start_markup,
                         )

    #работа со стартовыми кнопками
@router.callback_query(lambda c: c.data == 'about')
async def about_bot(callback: types.callback_query) -> None:
    await callback.message.answer(text=loader.about_project)
    await callback.answer()

@router.callback_query(lambda c: c.data == 'assistant_help')
async def ass_help(callback: types.callback_query) -> None:
    await callback.message.answer(text='тут должно быть чтото написано, но наш копирайтер чут чут даун ((((')
    await callback.answer()
@router.callback_query(lambda c: c.data == 'choose')
async def choose_profile(callback: types.callback_query) -> None:
    await callback.message.answer(text="Выберите профиль ассистента",
                                  reply_markup = loader.choose_markup)
    await callback.answer()

    #переключение на профиль

@router.callback_query(FSMContext(None),lambda c: c.data == 'profile_1')
async def profile_1_start(callback: types.callback_query,state:FSMContext):
    await state.set_state(States.Profile_1)
    await callback.message.answer('вы выбрали первый профиль! напишите хуйню - мы ответим')

@router.message(FSMContext(States.Profile_1),F.text)
async def profile_1_speaking(message: types.Message):


# ВСЕГДА НИЖЕ ВСЕХ !!!
@router.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.answer("Не знаю такой команды \n"
                             f"{hbold('/help')} - список доступных команд")
    except TypeError:
        await message.answer('Технические шоколадки!')