#(©)Codexbotz

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS, X_NUM
from helper_func import encode, get_message_id, convert

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


    textt = f"batch-{(f_msg_id * int(str(abs(client.db_channel.id))[8:]) + X_NUM)}-{(s_msg_id * int(str(abs(client.db_channel.id))[8:]) + X_NUM)}"
    string = await convert(textt)
    base64_string = await encode(string)
    base_64string = awiat base64_string.swapcase()
    link = f"t.me/{client.username}?start={base_64string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("• اشتراک گذاری لینک", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"🔗 لینک ایجاد شده برای فایل شما\n\n─══════─✦─══════─\n{link}\n─══════─✦─══════─\n\n🆔️ @{client.username}", quote=True, reply_markup=reply_markup, disable_web_page_preview = True)


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

    string = await convert(f"genlink-{(msg_id * int(str(abs(client.db_channel.id))[6:]) + X_NUM)}")
    base64_string = await encode(string)
    base_64string = awiat base64_string.swapcase()
    link = f"t.me/{client.username}?start={base_64string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("• اشتراک گذاری لینک", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"🔗 لینک ایجاد شده برای فایل شما\n\n─══════─✦─══════─\n{link}\n─══════─✦─══════─\n\n🆔️ @{client.username}", quote=True, reply_markup=reply_markup, disable_web_page_preview = True)
