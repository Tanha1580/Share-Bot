#(©)Codexbotz

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS, X_NUM
from helper_func import encode, get_message_id

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "📤 ارسال گروهی فایل‌ها\n\n⚜ پیام اول را از کانال دیتابیس فوروارد نمائید.\nیا لینک پیام را از کانال دیتابیس ارسال نمائید.", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ خطا\n\nاین [ پست / لینک ] از کانال دیتابیس نیست یا حذف شده است.", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "〽️ پیام آخر را از کانال دیتابیس فوروارد نمائید.\n\nیا لینک پیام را از کانال دیتابیس ارسال نمائید.", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ خطا\n\nاین [ پست / لینک ] از کانال دیتابیس نیست یا حذف شده است.", quote = True)
            continue


    string = f"{(f_msg_id * int(str(abs(client.db_channel.id))[3:]) + X_NUM)}-{(s_msg_id * int(str(abs(client.db_channel.id))[3:]) + X_NUM)}-{4}"
    base64_string = await encode(string)
    link = f"t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("• اشتراک گذاری لینک", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"🔗 لینک ایجاد شده برای فایل شما\n\n─═════─✦─═════─\n{link}", quote=True, reply_markup=reply_markup, disable_web_page_preview = True)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "🔰 ساخت لینک\n\n〽️ پیام مورد نظر را از کانال دیتابیس فوروارد نمائید.\nیا لینک پیام را از کانال دیتابیس ارسال نمائید.", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("❌ خطا\n\nاین [ پست / لینک ] از کانال دیتابیس نیست یا حذف شده است.", quote = True)
            continue

    base64_string = await encode(f"{(msg_id * int(str(abs(client.db_channel.id))[3:]) + X_NUM)}-{4}")
    link = f"t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("• اشتراک گذاری لینک", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"🔗 لینک ایجاد شده برای فایل شما\n\n─═════─✦─═════─\n{link}", quote=True, reply_markup=reply_markup, disable_web_page_preview = True)
