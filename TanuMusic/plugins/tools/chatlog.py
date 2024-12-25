from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from TanuMusic import app
from config import LOGGER_ID

@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = "Unable to fetch invite link (Insufficient Permissions)"
    try:
        # Attempt to get the invite link
        link = await app.export_chat_invite_link(chat.id)
    except Exception as e:
        # Log the exception for debugging
        print(f"Error exporting chat invite link: {e}")

    for members in message.new_chat_members:
        if members.id == (await app.get_me()).id:  # Check if the bot itself is added
            try:
                count = await app.get_chat_members_count(chat.id)
            except Exception as e:
                print(f"Error getting chat members count: {e}")
                count = "Unable to fetch member count"

            msg = (
                f"❖ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ #ɴᴇᴡ_ɢʀᴏᴜᴘ \n\n"
                f"● ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➥ {chat.title}\n"
                f"● ɢʀᴏᴜᴘ ɪᴅ ➥ {chat.id}\n"
                f"● ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ➥ @{chat.username if chat.username else 'Private Group'}\n"
                f"● ɢʀᴏᴜᴘ ʟɪɴᴋ ➥ {link}\n"
                f"● ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ➥ {count}\n\n"
                f"❖ ᴀᴅᴅᴇᴅ ʙʏ ➥ {message.from_user.mention if message.from_user else 'Unknown User'}"
            )
            await app.send_message(
                LOGGER_ID,
                text=msg,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("sᴇᴇ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɢʀᴏᴜᴘ", url=link if link != "Unable to fetch invite link (Insufficient Permissions)" else "https://t.me")]
                ])
            )

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "Unknown User"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "Private Chat"
        chat_id = message.chat.id
        left = (
            f"❖ <b>ʙᴏᴛ #ʟᴇғᴛ_ɢʀᴏᴜᴘ ʙʏ ᴀ ᴄʜᴜᴛɪʏᴀ</b> \n\n"
            f"● ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➥ {title}\n"
            f"● ɢʀᴏᴜᴘ ɪᴅ ➥ {chat_id}\n"
            f"● ʙᴏᴛ ʀᴇᴍᴏᴠᴇᴅ ʙʏ ➥ {remove_by}\n"
            f"❖ ʙᴏᴛ ɴᴀᴍᴇ ➥ ˹ ᴛᴀɴᴜ ꭙ ᴍᴜsɪᴄ™ ♡゙"
        )
        await app.send_message(
            LOGGER_ID,
            text=left,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{(await app.get_me()).username}?startgroup=true")]
            ])
        )