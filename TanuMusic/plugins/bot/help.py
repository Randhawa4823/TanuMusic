import random
from typing import Union
from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from TanuMusic import app
from TanuMusic.utils import help_pannel
from TanuMusic.utils.inline.help import help_back_markup, private_help_panel
from config import BANNED_USERS, SUPPORT_CHAT
from strings.helpers import help_1, help_2
from strings.image import Photos


@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except Exception:
            pass
        chat_id = update.message.chat.id
        # Removed language fetching, using default instead
        keyboard = help_pannel()  # No language required
        await update.edit_message_text(
            help_1.format(SUPPORT_CHAT), reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except Exception:
            pass
        # Removed language fetching, using default instead
        keyboard = help_pannel()  # No language required
        await update.reply_photo(
            random.choice(Photos),  # Randomly select an image
            caption=help_1.format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )


@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
async def help_com_group(client, message: Message):
    # Removed language parameter, using default helper panel
    keyboard = private_help_panel()  # No language required
    await message.reply_text(help_2, reply_markup=InlineKeyboardMarkup(keyboard))


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup()  # No language required
    if cb == "hb1":
        await CallbackQuery.edit_message_text(help_1, reply_markup=keyboard)
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(help_2, reply_markup=keyboard)
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(help_3, reply_markup=keyboard)
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(help_4, reply_markup=keyboard)
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(help_5, reply_markup=keyboard)
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(help_6, reply_markup=keyboard)
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(help_7, reply_markup=keyboard)
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(help_8, reply_markup=keyboard)
    elif cb == "hb9":
        await CallbackQuery.edit_message_text(help_9, reply_markup=keyboard)
    elif cb == "hb10":
        await CallbackQuery.edit_message_text(help_10, reply_markup=keyboard)
    elif cb == "hb11":
        await CallbackQuery.edit_message_text(help_11, reply_markup=keyboard)
    elif cb == "hb12":
        await CallbackQuery.edit_message_text(help_12, reply_markup=keyboard)
    elif cb == "hb13":
        await CallbackQuery.edit_message_text(help_13, reply_markup=keyboard)
    elif cb == "hb14":
        await CallbackQuery.edit_message_text(help_14, reply_markup=keyboard)
    elif cb == "hb15":
        await CallbackQuery.edit_message_text(help_15, reply_markup=keyboard)