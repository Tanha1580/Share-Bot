#(©)Codexbotz

import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

from bot import Bot
from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON, X_NUM
from helper_func import encode, subscribed

@Bot.on_message(filters.private & subscribed & ~filters.text & ~filters.sticker & ~filters.poll & ~filters.game)
async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("⏳ لطفا صبر کنید ...", quote = True)
    try:
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("❗️مشکلی رخ داد !")
        return
    converted_id = (post_message.message_id * int(str(abs(client.db_channel.id))[6:]) + X_NUM)
    string = f"{converted_id}"
    base64_string = await encode(string)
    link = f"t.me/{client.username}?start={base64_string}"

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("• اشتراک گذاری لینک", url=f'https://telegram.me/share/url?url={link}')]])

    await reply_text.edit(f"🔗 لینک ایجاد شده برای فایل شما\n\n─══════─✦─══════─\n{link}\n─══════─✦─══════─\n\n🆔️ @{client.username}", reply_markup=reply_markup, disable_web_page_preview = True)

    if not DISABLE_CHANNEL_BUTTON:
        await post_message.edit_reply_markup(reply_markup)

@Bot.on_message(filters.private & filters.user(ADMINS) & ~filters.command(['start','users','broadcast','batch','genlink']))
async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("⏳ لطفا صبر کنید ...", quote = True)
    try:
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("❗️مشکلی رخ داد !")
        return
    converted_id = (post_message.message_id * int(str(abs(client.db_channel.id))[6:]) + X_NUM)
    string = f"{converted_id}"
    base64_string = await encode(string)
    link = f"t.me/{client.username}?start={base64_string}"

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("• اشتراک گذاری لینک", url=f'https://telegram.me/share/url?url={link}')]])

    await reply_text.edit(f"🔗 لینک ایجاد شده برای فایل شما\n\n─══════─✦─══════─\n{link}\n─══════─✦─══════─\n\n🆔️ @{client.username}", reply_markup=reply_markup, disable_web_page_preview = True)

    if not DISABLE_CHANNEL_BUTTON:
        await post_message.edit_reply_markup(reply_markup)

@Bot.on_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID) & ~filters.edited)
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return

    converted_id = (message.message_id * int(str(abs(client.db_channel.id))[6:]) + X_NUM)
    string = f"{converted_id}"
    base64_string = await encode(string)
    link = f"t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("• اشتراک گذاری لینک", url=f'https://telegram.me/share/url?url={link}')]])
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
        pass
