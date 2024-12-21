from aiogram import Bot, Dispatcher, F
from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram.types import Message
from config import TOKEN




# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
# @dp.message()
# async def send_echo(message: Message):
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.reply(
#             text='Данный тип апдейтов не поддерживается '
#                  'методом send_copy'
#         )

# Фильтер на фото
@dp.message(F.photo)
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[-1].file_id)
# фильтер на текст
@dp.message(F.text)
async def send_echo(message: Message):
    await message.reply(text=message.text)
# фильтер на голосовые сообщения
@dp.message(F.voice)
async def send_echo(message: Message):
    await message.reply_voice(message.voice.file_id)
# Фильтер на видео
@dp.message(F.video)
async def send_echo(message: Message):
    await message.reply_video(message.video.file_id)
# Фильтер на стикер
@dp.message(F.sticker)
async def send_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)


if __name__ == '__main__':
    dp.run_polling(bot)