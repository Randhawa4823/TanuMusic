from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from TanuMusic import app

def help_pannel(START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text="Close", callback_data="close")]
    second = [
        InlineKeyboardButton(
            text="Back",
            callback_data="settingsback_helper",
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Admin",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="Auth",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="Broadcast",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Sudo",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="User",
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text="Song",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Quotly",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="Sticker",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="Image",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl

def help_back_markup():
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Back",
                    callback_data="settings_back_helper",
                ),
            ]
        ]
    )
    return upl

def private_help_panel():
    buttons = [
        [
            InlineKeyboardButton(
                text="Help and Commands",
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons