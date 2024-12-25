import time
import random
import pyrogram
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from TanuMusic import app
from strings.image import Photos
from TanuMusic.misc import _boot_
from TanuMusic.plugins.sudo.sudoers import sudoers_list
from TanuMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    is_banned_user,
    is_on_off,
)
from TanuMusic.utils.formatters import get_readable_time
from TanuMusic.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings.helpers import start_3, start_4, start_1, start_2, help_1


@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
async def start_pm(client, message: Message):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name.startswith("help"):
            keyboard = help_pannel()
            return await message.reply_photo(
                random.choice(Photos),
                caption=help_1.format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name.startswith("sud"):
            await sudoers_list(client=client, message=message)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"❖ {message.from_user.mention} just started the bot to check <b>sudolist</b>.\n\n"
                         f"<b>● User ID ➥</b> <code>{message.from_user.id}</code>\n"
                         f"<b>● Username ➥</b> @{message.from_user.username}",
                )
        if name.startswith("inf"):
            m = await message.reply_text("🔎 Searching...")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = (
                f"**Title:** {title}\n"
                f"**Duration:** {duration}\n"
                f"**Views:** {views}\n"
                f"**Published:** {published}\n"
                f"**Channel:** [{channel}]({channellink})\n"
                f"[Open on YouTube]({link})"
            )
            key = InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(text="YouTube", url=link),
                    InlineKeyboardButton(text="Support", url=config.SUPPORT_CHAT),
                ]]
            )
            await m.delete()
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"❖ {message.from_user.mention} just started the bot to check <b>track information</b>.\n\n"
                         f"<b>● User ID ➥</b> <code>{message.from_user.id}</code>\n"
                         f"<b>● Username ➥</b> @{message.from_user.username}",
                )
    else:
        out = private_panel()
        try:
            await message.reply_photo(
                random.choice(Photos),
                caption=start_2.format(message.from_user.mention, app.mention),
                reply_markup=InlineKeyboardMarkup(out),
            )
        except pyrogram.errors.exceptions.forbidden_403.ChatSendPhotosForbidden:
            await message.reply_text(
                start_2.format(message.from_user.mention, app.mention),
                reply_markup=InlineKeyboardMarkup(out),
            )
        if await is_on_off(2):
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"❖ {message.from_user.mention} just started the bot.\n\n"
                     f"<b>● User ID ➥</b> <code>{message.from_user.id}</code>\n"
                     f"<b>● Username ➥</b> @{message.from_user.username}",
            )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
async def start_gp(client, message: Message):
    out = start_panel()
    uptime = int(time.time() - _boot_)
    try:
        await message.reply_photo(
            random.choice(Photos),
            caption=start_1.format(app.mention, get_readable_time(uptime)),
            reply_markup=InlineKeyboardMarkup(out),
        )
    except pyrogram.errors.exceptions.forbidden_403.ChatSendPhotosForbidden:
        await message.reply_text(
            start_1.format(app.mention, get_readable_time(uptime)),
            reply_markup=InlineKeyboardMarkup(out),
        )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        if member.id == app.id:
            if message.chat.type != ChatType.SUPERGROUP:
                await message.reply_text(start_4)
                return await app.leave_chat(message.chat.id)
            if message.chat.id in await blacklisted_chats():
                await message.reply_text(
                    start_5.format(
                        app.mention,
                        f"https://t.me/{app.username}?start=sudolist",
                        config.SUPPORT_CHAT,
                    ),
                    disable_web_page_preview=True,
                )
                return await app.leave_chat(message.chat.id)

            out = start_panel()
            try:
                await message.reply_photo(
                    random.choice(Photos),
                    caption=start_3.format(
                        message.from_user.first_name,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            except pyrogram.errors.exceptions.forbidden_403.ChatSendPhotosForbidden:
                await message.reply_text(
                    start_3.format(
                        message.from_user.first_name,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            await add_served_chat(message.chat.id)
            await message.stop_propagation()