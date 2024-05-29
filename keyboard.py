from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from user_states import UserStates


def get_keyboard(buttons):
    kb = []
    for button in buttons:
        kb.append([KeyboardButton(text=button)])
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


keyboards = {
    UserStates.BASE: get_keyboard(["Мои пари", "Создать пари"])
}
