import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет')

@dp.message(Command("help"))
async def get_help(message: Message):
    await message.answer('Это команда /help')


@dp.message(Command("description"))
async def get_description(message: Message):
    await message.answer('При отправке команды "/start", бот здоровается\nПри отправки команды "/description" появляется описание бота')

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')