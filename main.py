from aiogram import Bot, Dispatcher, types, executor
import random
from config import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher(bot)

ran = random.randint(1, 3)

@dp.message_handler(commands = ['start'])
async def text(message: types.Message):
    await message.reply('Я загадал число от 1 до 3 угадайте')


@dp.message_handler()
async def rand(message: types.Message):
    if message.text == ran:
         await message.reply('Вы отгадали')
    else:
         await message.reply('Вы не отгадали')

executor.start_polling(dp)