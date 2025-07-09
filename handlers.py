from aiogram import Dispatcher, types, F
from aiogram.filters import CommandStart
from config import ADMIN_IDS
from keyboards import get_main_keyboard

async def start_handler(msg: types.Message):
    await msg.answer(
        "Assalomu alaykum hurmatli ota-ona!\n\nYuksalish maktabi faoliyatiga oid fikr va takliflaringiz bo‘lsa, iltimos shu yerga yozing.",
        reply_markup=get_main_keyboard()
    )

async def feedback_handler(msg: types.Message):
    user = msg.from_user
    feedback_text = f"✉️ Yangi fikr:\n\n👤 {user.full_name} (ID: {user.id})\n📩 {msg.text}"

    for admin_id in ADMIN_IDS:
        try:
            await msg.bot.send_message(chat_id=admin_id, text=feedback_text)
        except:
            pass

    await msg.answer("✅ Fikringiz uchun rahmat! Yuksalish maktabi jamoasi siz bilan bog‘lanadi.")

def register_handlers(dp: Dispatcher):
    dp.message.register(start_handler, CommandStart())
    dp.message.register(feedback_handler, F.text)
