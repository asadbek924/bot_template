from aiogram.types.inline_keyboard import InlineKeyboardButton,InlineKeyboardMarkup

test_in_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="test1",callback_data="Asadbek")],
        [InlineKeyboardButton(text="test2",callback_data="Sunnat")],
        [InlineKeyboardButton(text="link",url="https://t.me/+Jj3lWOWQoGs1Y2Ri")],
        [InlineKeyboardButton(text="Tasodif",callback_data="random")]
    ]
)
def raqam_kb():
    tugmalar=[]
    for i in range(1,10):
        tugmalar.append(InlineKeyboardButton(text=f"{i}", callback_data=f"raqam_{i}"))
    kb=InlineKeyboardMarkup(row_width=3)
    kb.add(*tugmalar)
    return kb