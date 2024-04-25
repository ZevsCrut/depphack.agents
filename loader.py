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
choose_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=emojize(':man_scientist: Профиль 1'),callback_data='profile_1')],
        [InlineKeyboardButton(text=emojize(':man_scientist: Профиль 2'),callback_data='profile_2')],
        [InlineKeyboardButton(text=emojize(':man_scientist: Профиль 3'),callback_data='profile_3')]
    ]
)
text1 = ("🔬 Приветствую вас в научном ассистенте, вашем надежном помощнике в мире исследований и разработок!\n"
         " Этот бот создан, чтобы помочь ученым, исследователям и студентам упростить процесс научной работы и повысить эффективность их исследований.")
about_project = ("📚 Возможности бота:\n\n"
"📃 Поиск академических статей: Получите самые последние публикации по вашему запросу из различных научных баз данных.\n"
"🧬 Данные экспериментов: Быстрый доступ к наборам данных и статистическим ресурсам для вашего исследования.\n"
"⚙️ Инструменты анализа: Бот может предоставить вам и для качественного и количественного анализа данных.\n"
"📘 Литературные обзоры: Автоматическая сборка обзоров литературы и аннотаций, помогающая выделить ключевые работы в вашей области.\n"
"🎓 Форматирование ссылок: Помощь в автоматическом форматировании библиографических ссылок в соответствии с выбранным стилевым руководством (APA, MLA, Chicago и др.)\n"
"🧪 Протоколы экспериментов: Доступ к сохранённым методикам и стандартным операционным процедурам лабораторных исследований.\n"
"🔎 Подбор журналов для публикации: Рекомендации относительно наиболее подходящих журналов для вашей следующей статьи.\n"
"🚀 Как начать работу:")