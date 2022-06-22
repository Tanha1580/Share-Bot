#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, ABOUT_MSG
from .start import HELP_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    id = query.from_user.id
    data = query.data
    if data == "about":
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❌ بستن", callback_data = "close")
                ]
            ]
        )
        reply_markup_admin = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📃 راهنمای ربات", callback_data = "help"),
                    InlineKeyboardButton("❌ بستن", callback_data = "close")
                ]
            ]
        )
        await query.message.edit_text(
            text = ABOUT_MSG,
            disable_web_page_preview = True,
            reply_markup = reply_markup_admin if query.from_user.id in ADMINS else reply_markup
        )
    elif data == "help":
        await query.message.edit_text(
            text = HELP_MSG,
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("❌ بستن", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
