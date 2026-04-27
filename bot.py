import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import LabeledPrice, PreCheckoutQuery


TOKEN = "8763920094:AAE_2_OzL3DXm9Q0_T7tKdCHtgmMYy43iEw"

bot = Bot(token=TOKEN)
dp = Dispatcher()

vip_users = set()

# /start
@dp.message(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "👋 Bienvenue !\n\n"
        "⭐ Accès VIP disponible : 50 Stars\n"
        "Tape /buy pour acheter"
    )

# /buy (Stars)
@dp.message(commands=["buy"])
async def buy(message: types.Message):
    prices = [LabeledPrice(label="VIP Access", amount=50)]

    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Accès VIP",
        description="Débloque le contenu premium",
        payload="vip_access",
        provider_token="",  # IMPORTANT : vide pour Stars
        currency="XTR",
        prices=prices
    )

# validation paiement
@dp.pre_checkout_query()
async def pre_checkout(pre_checkout_q: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

# après paiement
@dp.message(lambda message: message.successful_payment)
async def success(message: types.Message):
    vip_users.add(message.from_user.id)
    await message.answer("✅ Paiement réussi ! Tu es VIP ⭐")

# contenu VIP
@dp.message(commands=["vip"])
async def vip(message: types.Message):
    if message.from_user.id in vip_users:
        await message.answer("🎁 Contenu VIP débloqué !")
    else:
        await message.answer("❌ Accès refusé. Fais /buy")

# lancement bot
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
