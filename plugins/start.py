#(©)CodeXBotz
import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from bot import Bot
from config import ADMINS, FORCE_MSG, START_MSG, OWNER_ID, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, PROTECT_CONTENT, X_NUM
from .button import fsub_button
from helper_func import subscribed, subch1, subch2, subch3, subch4, encode, decode, get_messages, convert, reconvert, cconvert, convertt
from database.sql import add_user, query_msg, full_userbase


#=====================================================================================##

WAIT_MSG = """⚙ در حال پردازش ..."""

GET_MSG = """<b>𝖴𝗌𝖾𝗋 𝖨𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇</b>
 ├ Fʀᴏᴍ <a href='tg://user?id={id}'>🅨︎🅞︎🅤︎</a>
 ┊├ 𝖣𝖢: {dc}
 ┊├ 𝖨𝖣: <code>{id}</code>
 ┊├ 𝖥𝗂𝗋𝗌𝗍 𝖭𝖺𝗆𝖾: {first}
 ┊├ 𝖫𝖺𝗌𝗍 𝖭𝖺𝗆𝖾: {last}
 ┊└ 𝖴𝗌𝖾𝗋 𝖭𝖺𝗆𝖾: {username}
 ┊
 └ 𝗣𝗿𝗼𝗱𝘂𝗰𝘁 𝗯𝘆 𝗙𝗼𝗻𝘁𝗴𝗮𝗵𝗧𝗲𝗮𝗺
"""

REPLY_ERROR = """📢 اطلاع‌رسانی\n\nروی پیام مورد نظر ریپلای نمائید و مجدد <code>/broadcast</code> را ارسال کنید."""

REPLYERROR = """📢 فوروارد پیام\n\nروی پیام مورد نظر ریپلای نمائید و مجدد <code>/forward</code> را ارسال کنید."""

HELP_MSG = """‎📃راهنمای دستورات ربات:

‎◌ /users ↴
  ᴥ دریافت آمار کاربران ربات

‎◌ /id ↴
  ᴥ دریافت اطلاعات کاربر

‎◌ /senderid ↴
  ᴥ دریافت اطلاعات پست

‎◌ /broadcast ↴
  ᴥ ارسال پیام به کاربران ربات

‎◌ /forward ↴
  ᴥ فوروارد پیام به کاربران ربات

‎◌ /genlink ↴
  ᴥ ساخت لینک برای پست کانال

‎◌ /batch ↴
  ᴥ لینک ارسال گروهی فایل

‎◌ /help ↴
  ᴥ راهنمای ربات
"""

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
            texxt = text.split(" ", 1)[1]
            base64_string = await convertt(texxt)
        except:
            return
        try:
           ttext = await decode(base64_string)
        except:
            bvv = await message.reply("⛔ شناسه فایل اشتباه است.")
            await asyncio.sleep(3)
            await bvv.delete()
            return
        string = await reconvert(ttext)
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
            cw = argument[0]
            if cw.isdecimal() == True:
                try:
                    ids = [int((int(argument[1]) - X_NUM) / int(str(abs(client.db_channel.id))[6:]))]
                except:
                    return
            else:
                bv = await message.reply("⛔ شناسه فایل اشتباه است.")
                await asyncio.sleep(3)
                await bv.delete()
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

                if font:
                    await asyncio.sleep(0.3)
                    ms = await message.reply("⏳ پیام بالا تا <u>30</u> ثانیه دیگر حذف میشود!\nلطفا قبل از حذف شدن پیام، آن را در Saved Messages تلگرام خود ذخیره کنید.")
                    await asyncio.sleep(10)
                    await ms.edit("⏳ پیام بالا تا <u>20</u> ثانیه دیگر حذف میشود!\nلطفا قبل از حذف شدن پیام، آن را در Saved Messages تلگرام خود ذخیره کنید.")
                    await asyncio.sleep(10)
                    await ms.edit("⏳ پیام بالا تا <u>10</u> ثانیه دیگر حذف میشود!\nلطفا قبل از حذف شدن پیام، آن را در Saved Messages تلگرام خود ذخیره کنید.")
                    await asyncio.sleep(10)
                    await font.delete()
                    await asyncio.sleep(0.2)
                    await ms.edit(f"🚮 پیام حذف شد.\n\n<b>Message_id:</b> {texxt}")
                    await asyncio.sleep(4)
                    await ms.delete()
                else:
                    pg = await message.reply(f"⚠️ خطا در دریافت پیام!\n\n⭕ پیام مورد نظر توسط ادمین ربات، از دیتابیس ربات حذف گردیده است!\n<b>Message_ID:</b> <s>{texxt}</s>")
                    await asyncio.sleep(3)
                    await pg.delete()
            except FloodWait as e:
                await asyncio.sleep(e.x)
                fontt = await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = 'html', reply_markup = reply_markup, protect_content=PROTECT_CONTENT)

                if fontt:
                    await asyncio.sleep(0.3)
                    mss = await message.reply("⏳ پیام بالا تا <u>30</u> ثانیه دیگر حذف میشود!\nلطفا قبل از حذف شدن پیام، آن را در Saved Messages تلگرام خود ذخیره کنید.")
                    await asyncio.sleep(10)
                    await mss.edit("⏳ پیام بالا تا <u>20</u> ثانیه دیگر حذف میشود!\nلطفا قبل از حذف شدن پیام، آن را در Saved Messages تلگرام خود ذخیره کنید.")
                    await asyncio.sleep(10)
                    await mss.edit("⏳ پیام بالا تا <u>10</u> ثانیه دیگر حذف میشود!\nلطفا قبل از حذف شدن پیام، آن را در Saved Messages تلگرام خود ذخیره کنید.")
                    await asyncio.sleep(10)
                    await fontt.delete()
                    await asyncio.sleep(0.2)
                    await mss.edit(f"🚮 پیام حذف شد.\n\n<b>Message_id:</b> {texxt}")
                    await asyncio.sleep(4)
                    await mss.delete()
                else:
                    pgg = await message.reply(f"⚠️ خطا در دریافت پیام!\n\n⭕ پیام مورد نظر توسط ادمین ربات، از دیتابیس ربات حذف گردیده است!\n<b>Message_ID:</b> <s>{texxt}</s>")
                    await asyncio.sleep(3)
                    await pgg.delete()
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
        reply_markup_admin = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📃 راهنمای ربات", callback_data = "help"),
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
            reply_markup = reply_markup_admin if id in ADMINS else reply_markup,
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

@Bot.on_message(filters.command('help') & filters.private & filters.user(ADMINS))
async def help(client: Bot, message: Message):
    await message.reply(
        text = HELP_MSG,
        quote = True,
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("❌ بستن", callback_data = "close")]])
    )

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

@Bot.on_message(filters.private & filters.command('forward') & filters.user(ADMINS))
async def forward_message(client: Bot, message: Message):
    if message.reply_to_message:
        query = await query_msg()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("📢 فوروارد پیام\nاین عمل ممکن است کمی طول بکشد ...")
        for row in query:
            chat_id = int(row[0])
            try:
                await broadcast_msg.forward(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.forward(chat_id)
                successful += 1
            except UserIsBlocked:
                blocked += 1
            except InputUserDeactivated:
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""✅ فوروارد پیام کامل شد

<b>• تعداد کاربران: <code>{total}</code>
• موفق: <code>{successful}</code>
• کاربران مسدود کرده: <code>{blocked}</code>
• کاربران حذف شده: <code>{deleted}</code>
• ناموفق: <code>{unsuccessful}</code></b>"""
        
        return await pls_wait.edit(status)

    else:
        msg = await message.reply(REPLYERROR)
        await asyncio.sleep(8)
        await msg.delete()

@Bot.on_message(filters.private & filters.command('senderid') & filters.user(ADMINS))
async def id_command(client: Client, message: Message):
    text = message.text
    if len(text)>10:
        try:
            texxt = text.split(" ", 1)[1]
            base64_string = await convertt(texxt)
        except:
            return
        try:
            ttext = await decode(base64_string)
        except:
            bbv = await message.reply("⛔ شناسه فایل اشتباه است.")
            await asyncio.sleep(3)
            await bbv.delete()
            return
        string = await reconvert(ttext)
        argument = string.split("-")
        if len(argument) == 3:
            start = int((int(argument[1]) - X_NUM) / int(str(abs(client.db_channel.id))[8:]))
            end = int((int(argument[2]) - X_NUM) / int(str(abs(client.db_channel.id))[8:]))
            await message.reply(f"🔰 این لینک مربوط به ارسال گروهی فایل بوده و توسط ادمین ربات ساخته شده است.\n\n🔗 لینک پست در کانال دیتابیس:\n<a href='https://t.me/c/{str(abs(client.db_channel.id))[3:]}/{start}'>Start:{start}</a> , <a href='https://t.me/c/{str(abs(client.db_channel.id))[3:]}/{end}'>End:{end}</a>\n─═══─✦─═══─\n𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋: <a href='https://t.me/Ali4702'>𝙰𝚕𝚒😎</a>", disable_web_page_preview = True, quote = True)
        elif len(argument) == 2:
            nm = argument[0]
            ids = int((int(argument[1]) - X_NUM) / int(str(abs(client.db_channel.id))[6:]))
            if nm == "Example":
                await message.reply("🆔 آیدی عددی صاحب پیام :\n[ <code>Example</code> ]\n─══════─✦─══════─\n🔗 لینک پست در کانال دیتابیس:\nhttps://t.me/c/Channel_ID/Post_ID", quote = True)
            if nm == "12":
                await message.reply(f"🔰 این لینک مربوط به دستور /genlink و توسط ادمین‌های ربات ساخته شده است.\n\n🔗 لینک پست در کانال دیتابیس:\n<a href='https://t.me/c/{str(abs(client.db_channel.id))[3:]}/{ids}'>Goto:{ids}</a>\n─══─✦─══─\n𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋: <a href='https://t.me/Ali4702'>𝙰𝚕𝚒😎</a>", disable_web_page_preview = True, quote = True)
            if nm == "13":
                await message.reply(f"🔰 این لینک مربوط به ارسال فایل به صورت مستقیم در کانال توسط ادمین میباشد.\n\n🔗 لینک پست در کانال دیتابیس:\n<a href='https://t.me/c/{str(abs(client.db_channel.id))[3:]}/{ids}'>Goto:{ids}</a>\n─══─✦─══─\n𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋: <a href='https://t.me/Ali4702'>𝙰𝚕𝚒😎</a>", disable_web_page_preview = True, quote = True)
            if not nm == "13" and not nm == "12" and len(nm)>7:
                await message.reply(f"🆔 آیدی عددی صاحب پیام :\n[ <code>{nm}</code> ]\n─══════─✦─══════─\n🔗 لینک پست در کانال دیتابیس:\n<a href='https://t.me/c/{str(abs(client.db_channel.id))[3:]}/{ids}'>Goto:{ids}</a>\n─══─✦─══─\n𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋: <a href='https://t.me/Ali4702'>𝙰𝚕𝚒😎</a>", disable_web_page_preview = True, quote = True)
            if not nm == "13" and not nm == "12" and not len(nm)>7 and not nm == "Example":
                await message.reply(f"🆔 آیدی عددی صاحب پیام (نامتعارف):\n[ <code>{nm}</code> ]\n─══════─✦─══════─\n🔗 لینک پست در کانال دیتابیس:\n<a href='https://t.me/c/{str(abs(client.db_channel.id))[3:]}/{ids}'>Goto:{ids}</a>\n─══─✦─══─\n𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋: <a href='https://t.me/Ali4702'>𝙰𝚕𝚒😎</a>", disable_web_page_preview = True, quote = True)
    else:
        fd = await message.reply("⚠️ خطا\n\nدستور اشتباه است!\nاز دستور /senderid همراه با شناسه فایل استفاده کنید\n\nمثال:\n/senderid EKhhbKOsMF0xZjZ0", quote = True)
        await asyncio.sleep(15)
        await fd.delete()

@Bot.on_message(filters.command('id') & filters.private)
async def get_info(client: Client, message: Message):
    await message.reply(
        text = GET_MSG.format(
                first = message.from_user.first_name,
                last = "- - - - -" if not message.from_user.last_name else message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                dc = message.from_user.dc_id,
                id = message.from_user.id
            ),
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("❌ بستن", callback_data = "close")]]),
        quote = True,
        disable_web_page_preview = True
    )
