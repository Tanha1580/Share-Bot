#(©)CodeXBotz
import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from bot import Bot
from config import ADMINS, FORCE_MSG, START_MSG, OWNER_ID, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, PROTECT_CONTENT, X_NUM
from .button import fsub_button
from helper_func import subscribed, subch1, subch2, subch3, subch4, encode, decode, get_messages
from database.sql import add_user, query_msg, full_userbase


#=====================================================================================##

WAIT_MSG = """"⚙ در حال پردازش ..."""

REPLY_ERROR = """📢 اطلاع‌رسانی\n\nروی پیام مورد نظر ریپلای نمائید و مجدد <code>/broadcast</code> را ارسال کنید."""

#=====================================================================================##


@Bot.on_message(filters.command('start') & filters.private & subscribed & subch1 & subch2 & subch3 & subch4)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    user_name = '@' + message.from_user.username if message.from_user.username else None
    try:
        await add_user(id, user_name)
    except:
        pass
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int((int(argument[1]) - X_NUM) / int(str(abs(client.db_channel.id))[8:]))
                end = int((int(argument[2]) - X_NUM) / int(str(abs(client.db_channel.id))[8:]))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int((int(argument[1]) - X_NUM) / int(str(abs(client.db_channel.id))[6:]))]
            except:
                return
        temp_msg = await message.reply("⏳ لطفا صبر کنید ...")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("❗️مشکلی رخ داد !")
            return
        await temp_msg.delete()

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = msg.reply_markup
            else:
                reply_markup = None

            try:
                font = await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = 'html', reply_markup = reply_markup, protect_content=PROTECT_CONTENT)
                await asyncio.sleep(0.3)
                ms = await message.reply("پیام بالا تا 30 ثانیه دیگر پاک میشود. لطفا قبل از پاک شدن آن را در saved messages تلگرام خود ذخیره کنید.")
                await asyncio.sleep(30)
                await font.delete()
                await asyncio.sleep(0.2)
                await ms.delete()
                fd = await message.reply("پیام حذف شد.")
                await asyncio.sleep(15)
                await fd.delete()
            except FloodWait as e:
                await asyncio.sleep(e.x)
                fontt = await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = 'html', reply_markup = reply_markup, protect_content=PROTECT_CONTENT)
                await asyncio.sleep(0.3)
                mss = await message.reply("پیام بالا تا 30 ثانیه دیگر پاک میشود. لطفا قبل از پاک شدن آن را در saved messages تلگرام خود ذخیره کنید.")
                await asyncio.sleep(30)
                await fontt.delete()
                await asyncio.sleep(0.2)
                await mss.delete()
                fdd = await message.reply("پیام حذف شد.")
                await asyncio.sleep(15)
                await fdd.delete()
            except:
                pass
        return
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🤖 دربارۀ ربات", callback_data = "about")
                ]
            ]
        )
        await message.reply_text(
            text = START_MSG.format(
                first = message.from_user.first_name,
                last = "" if not message.from_user.last_name else ' ' + message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            disable_web_page_preview = True,
            quote = True
        )
        return

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    buttons = fsub_button(client, message)
    await message.reply(
        text = FORCE_MSG.format(
                first = message.from_user.first_name,
                last = "" if not message.from_user.last_name else ' ' + message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
        reply_markup = InlineKeyboardMarkup(buttons),
        quote = True,
        disable_web_page_preview = True
    )

@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"👤 {len(users)} نفر از ربات استفاده می‌کنند.")

@Bot.on_message(filters.private & filters.command('id') & filters.user(ADMINS))
async def id_command(client: Client, message: Message):
    text = message.text
    if len(text)>4:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                us_er = [int(argument[0])]
        elif len(argument) == 2:
            try:
                us_er = [int(argument[0])]
        except:
            await message.reply("❗️مشکلی رخ داد !")
        return
    await message.reply(f"آیدی صاحب پیام: <code>{us_er}</code>", quote = True)

@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await query_msg()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("📢 پیام اطلاع‌رسانی\nاین عمل ممکن است کمی طول بکشد ...")
        for row in query:
            chat_id = int(row[0])
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                blocked += 1
            except InputUserDeactivated:
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""✅ اطلاع‌رسانی کامل شد

<b>• تعداد کاربران: <code>{total}</code>
• موفق: <code>{successful}</code>
• کاربران مسدود کرده: <code>{blocked}</code>
• کاربران حذف شده: <code>{deleted}</code>
• ناموفق: <code>{unsuccessful}</code></b>"""
        
        return await pls_wait.edit(status)

    else:
        msg = await message.reply(REPLY_ERROR)
        await asyncio.sleep(8)
        await msg.delete()
