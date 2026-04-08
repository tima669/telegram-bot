import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Твій токен
TOKEN = "8267849382:AAESa13qaF20kiqMdyM0ZT4KSpvOTCclUXc"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Налаштування клавіатури
def main_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="💊 Замовити вітамінки")
    builder.button(text="📜 Почитати рецепт")
    builder.button(text="🧪 Зайти в лабораторію")
    builder.button(text="🩹 Потрібен пластир (Допомога)")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

# Обробник команди /start
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Вітаю у нашій цифровій аптеці, {message.from_user.first_name}! 🏥\n\n"
        "Ваш рецепт уже прострочений, але ми щось придумаємо. "
        "Обирайте препарат на клавіатурі нижче. Обережно, побічний ефект — гарний настрій!",
        reply_markup=main_menu()
    )

# Обробник команди /help (у стилі аптеки)
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "Інструкція до застосування бота:\n"
        "1. Не натискайте всі кнопки одночасно (можливе передозування кодом).\n"
        "2. Якщо бот тупить — це не баг, це черга в державній аптеці.\n"
        "3. Пишіть будь-що, і ми підберемо вам подорожник."
    )

# Обробка натискань кнопок
@dp.message(F.text == "💊 Замовити вітамінки")
async def vitamins(message: types.Message):
    await message.answer("Сорі, вітамінки закінчилися. Залишився тільки активоване вугілля з підсвіткою (RGB-версія). Берете?")

@dp.message(F.text == "📜 Почитати рецепт")
async def recipe(message: types.Message):
    await message.answer(
        "Ваш рецепт:\n"
        "— Python 3.10 (вживати щодня)\n"
        "— Чистий код (натщесерце)\n"
        "— Сон (0 мг, відпускається тільки за спецдозволом)"
    )

@dp.message(F.text == "🧪 Зайти в лабораторію")
async def lab(message: types.Message):
    await message.answer("Тут ми розробляємо вакцину від помилок `IndexError`. Робота триває, не дихайте на пробірки!")

# Відповідь на будь-яке інше повідомлення (ехо-бот з гумором)
@dp.message()
async def echo_pharmacy(message: types.Message):
    phrases = [
        "Ваш почерк занадто зрозумілий, я не можу це прочитати.",
        "Цього препарату немає в наявності, візьміть гематогенку.",
        "Ого, це серйозний запит. Тут одним подорожником не обійдешся.",
        "Вибачте, у нас переоблік бази даних. Зайдіть через 15 наносекунд."
    ]
    import random
    await message.reply(random.choice(phrases))

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Аптека зачинена на перерву.")