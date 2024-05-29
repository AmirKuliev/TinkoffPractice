from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN
from keyboard import keyboards
from user_states import UserStates
import asyncio


storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)


@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    kb = keyboards[UserStates.BASE]
    await message.answer("Привет! Я умею следить за PariMatch!", reply_markup=kb)
    await state.set_state(UserStates.BASE)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("Bot has been started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
