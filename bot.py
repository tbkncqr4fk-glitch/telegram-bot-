import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "
8763920094:AAE_2_OzL3DXm9Q0_T7tKdCHtgmMYy43iEw"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(commands=["start"])
async def start(message: types.Message):
    await message.answer("👋 Bot en ligne")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
