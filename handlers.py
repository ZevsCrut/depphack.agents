from loader import bot, TOKEN

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


from loader import dp, start_markup,router





@router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext) -> None:
    try:
        await state.clear
    except:
        pass
    logo = types.FSInputFile('start_logo.png')
    await bot.send_photo(chat_id=message.chat.id, photo=logo,
                         caption=f'Привет,{hbold(message.from_user.full_name)}!\n'
                                 f'Я - твой личный помощник для выполнения любых научных задач',
                         reply_markup=start_markup,
                         )


#ВСЕГДА НИЖЕ ВСЕХ !!!
@router.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.answer("Не знаю такой команды \n"
                             f"{hbold('/help')} - список доступных команд")
    except TypeError:
        await message.answer('Технические шоколадки!')