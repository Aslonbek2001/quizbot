from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
# Bot token
API_TOKEN = "6146364132:AAE8Ox52l6kH_uXXcD2AIqcFWadI0AXBBTw"
# Bot va Dispatcher'ni sozlash
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
# Start komandasi uchun handler
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Salom! \n Men Savollaringizga javob bera olaman qanday savolingiz bor!")        
    
# Matnli xabarlar uchun handler
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Sizning savol quyidagicha:\n {message.text}")
    await message.answer(f"Bu biroz vaqt olishi mumkin :)")
    
# Botni ishga tushirish
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



@dp.message()
async def my_handler(message: types.Message):
    if "Bugun havo qanday?" == message.text:
        await message.answer("Bugun havo -5 - 10 daraja o'rtasida")
    elif "Isming nima" in message.text:
        await message.answer("Men Botman")
    elif "Qalesan" == message.text:
        await message.answer("Ajoyib")
    elif "Nima gap" == message.text:
        await message.answer("Tinchlik")
    else:
        await message.answer("Bu savolga javob berolmayman")