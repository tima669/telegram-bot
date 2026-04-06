import asyncio
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '8267849382:AAESa13qaF20kiqMdyM0ZT4KSpvOTCclUXc'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Цікавий факт 💡")],
        [KeyboardButton(text="Мій розклад 📅"), KeyboardButton(text="Налаштування ⚙️")]
    ],
    resize_keyboard=True
)

settings_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Мова 🌐", callback_data="st"), InlineKeyboardButton(text="Звук 🔔", callback_data="st")],
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="go_back")]
])

quiz_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1991", callback_data="q_no"),
        InlineKeyboardButton(text="988", callback_data="q_yes"),
        InlineKeyboardButton(text="1240", callback_data="q_no")
    ]
])


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Йо, {message.from_user.first_name}! 👋 Я твій помічник. Го погнали!", reply_markup=main_kb)


@dp.message(Command("help"))
async def help(message: types.Message):
    await message.answer("Дивись, що можу:\n/start - запуск\n/quiz - вікторина\n/about - хто я\n/menu - кнопки")


@dp.message(Command("about"))
async def about(message: types.Message):
    await message.answer("Дев: Тимофій Філіпчук 😎\nВерсія: 1.2 (Senior)")


@dp.message(Command("menu"))
async def menu(message: types.Message):
    await message.answer("Тримай кнопки 👇", reply_markup=main_kb)


@dp.message(Command("quiz"))
async def quiz(message: types.Message):
    await message.answer("Коли хрестили Русь? 🤔", reply_markup=quiz_kb)


@dp.callback_query(F.data.startswith("q_"))
async def q_callback(call: types.CallbackQuery):
    if call.data == "q_yes":
        await call.answer("Красава! ✅", show_alert=True)
        await call.message.edit_text("Шариш в історії! ✨")
    else:
        await call.answer("Не вгадав, спробуй ще! ❌", show_alert=True)


@dp.callback_query(F.data == "go_back")
async def back(call: types.CallbackQuery):
    await call.message.edit_text("Ок, повернулися назад. Юзай меню! 👇")


@dp.message(F.text)
async def chat(message: types.Message):
    txt = message.text.lower()

    if "привіт" in txt:
        await message.reply(f"Привіт, {message.from_user.first_name}! Що там нового?")