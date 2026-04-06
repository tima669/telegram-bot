import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

API_TOKEN = "8267849382:AAESa13qaF20kiqMdyM0ZT4KSpvOTCclUXc"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привіт, я твій бот! Напиши /help, щоб дізнатися, що я вмію.")

# /help
@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Команди:\n/start — запуск\n/help — допомога\n/joke — жарт\n/bye — прощання")

# /joke
@dp.message(Command("joke"))
async def joke_command(message: Message):
    await message.answer("Чому комп’ютер пішов у спортзал? Щоб прокачати свої байти!")

# /bye
@dp.message(Command("bye"))
async def bye_command(message: Message):
    await message.answer("До побачення! Гарного дня 😊")

# Обробка звичайного тексту
@dp.message()
async def echo_text(message: Message):
    text = message.text.lower()
    if "привіт" in text:
        await message.answer("Привіт! Гарного настрою 😄")
    elif "як справи" in text:
        await message.answer("У мене все супер, дякую! А в тебе?")
    else:
        await message.answer("Я ще вчуся, тому не знаю як відповісти на це 😅")

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())