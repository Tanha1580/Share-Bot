#(©)CodeXBotz
from config import FORCE_SUB_CHANNEL_1, FORCE_SUB_CHANNEL_2, FORCE_SUB_CHANNEL_3, FORCE_SUB_CHANNEL_REQUEST_1, FORCE_SUB_CHANNEL_REQUEST_2, FORCE_SUB_CHANNEL_REQUEST_3
from pyrogram.types import InlineKeyboardButton


def fsub_button(client, message):
    if FORCE_SUB_CHANNEL_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_CHANNEL_3 and not FORCE_SUB_CHANNEL_REQUEST_1 and not FORCE_SUB_CHANNEL_REQUEST_2 and not FORCE_SUB_CHANNEL_REQUEST_3:
        buttons = [
            [
                InlineKeyboardButton(text = "• عضویت اول", url = client.invitelink1)
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(text = "• عضو شدم | دانلود فایل", url = f"https://t.me/{client.username}?start={message.command[1]}")
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL_1 and FORCE_SUB_CHANNEL_2 and not FORCE_SUB_CHANNEL_3 and not FORCE_SUB_CHANNEL_REQUEST_1 and not FORCE_SUB_CHANNEL_REQUEST_2 and not FORCE_SUB_CHANNEL_REQUEST_3:
        buttons = [
            [
                InlineKeyboardButton(text = "• عضویت اول", url = client.invitelink1)
            ],
            [
                InlineKeyboardButton(text = "• عضویت دوم", url = client.invitelink2)
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(text = "• عضو شدم | دانلود فایل", url = f"https://t.me/{client.username}?start={message.command[1]}")
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL_1 and FORCE_SUB_CHANNEL_2 and FORCE_SUB_CHANNEL_3 and not FORCE_SUB_CHANNEL_REQUEST_1 and not FORCE_SUB_CHANNEL_REQUEST_2 and not FORCE_SUB_CHANNEL_REQUEST_3:
        buttons = [
            [
                InlineKeyboardButton(text = "• عضویت اول", url = client.invitelink1)
            ],
            [
                InlineKeyboardButton(text = "• عضویت دوم", url = client.invitelink2)
            ],
            [
                InlineKeyboardButton(text = "• عضویت سوم", url = client.invitelink3)
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(text = "• عضو شدم | دانلود فایل", url = f"https://t.me/{client.username}?start={message.command[1]}")
                ]
            )
        except IndexError:
            pass
        return buttons
    if not FORCE_SUB_CHANNEL_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_CHANNEL_3 and FORCE_SUB_CHANNEL_REQUEST_1 and not FORCE_SUB_CHANNEL_REQUEST_2 and not FORCE_SUB_CHANNEL_REQUEST_3:
        buttons = [
            [
                InlineKeyboardButton(text = "• عضویت اول", url = client.reinvitelink1)
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(text = "• عضو شدم | دانلود فایل", url = f"https://t.me/{client.username}?start={message.command[1]}")
                ]
            )
        except IndexError:
            pass
        return buttons
    if not FORCE_SUB_CHANNEL_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_CHANNEL_3 and FORCE_SUB_CHANNEL_REQUEST_1 and FORCE_SUB_CHANNEL_REQUEST_2 and not FORCE_SUB_CHANNEL_REQUEST_3:
        buttons = [
            [
                InlineKeyboardButton(text = "• عضویت اول", url = client.reinvitelink1)
            ],
            [
                InlineKeyboardButton(text = "• عضویت دوم", url = client.reinvitelink2)
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(text = "• عضو شدم | دانلود فایل", url = f"https://t.me/{client.username}?start={message.command[1]}")
                ]
            )
        except IndexError:
            pass
        return buttons
    if not FORCE_SUB_CHANNEL_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_CHANNEL_3 and FORCE_SUB_CHANNEL_REQUEST_1 and FORCE_SUB_CHANNEL_REQUEST_2 and FORCE_SUB_CHANNEL_REQUEST_3:
        buttons = [
            [
                InlineKeyboardButton(text = "• عضویت اول", url = client.reinvitelink1)
            ],
            [
                InlineKeyboardButton(text = "• عضویت دوم", url = client.reinvitelink2)
            ],
            [
                InlineKeyboardButton(text = "• عضویت سوم", url = client.reinvitelink3)
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(text = "• عضو شدم | دانلود فایل", url = f"https://t.me/{client.username}?start={message.command[1]}")
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_CHANNEL_3 and not FORCE_SUB_CHANNEL_REQUEST_1 and FORCE_SUB_CHANNEL_REQUEST_2 and not FORCE_SUB_CHANNEL_REQUEST_3:
        buttons = [
            [
                InlineKeyboardButton(text = "• عضویت اول", url = client.invitelink1)
            ],
            [
                InlineKeyboardButton(text = "• عضویت دوم", url = client.reinvitelink2)
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(text = "• عضو شدم | دانلود فایل", url = f"https://t.me/{client.username}?start={message.command[1]}")
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL_1 and not FORCE_SUB_CHANNEL_2 and not FORCE_SUB_CHANNEL_3 and not FORCE_SUB_CHANNEL_REQUEST_1 and FORCE_SUB_CHANNEL_REQUEST_2 and FORCE_SUB_CHANNEL_REQUEST_3:
        buttons = [
            [
                InlineKeyboardButton(text = "• عضویت اول", url = client.invitelink1)
            ],
            [
                InlineKeyboardButton(text = "• عضویت دوم", url = client.reinvitelink2)
            ],
            [
                InlineKeyboardButton(text = "• عضویت سوم", url = client.reinvitelink3)
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(text = "• عضو شدم | دانلود فایل", url = f"https://t.me/{client.username}?start={message.command[1]}")
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL_1 and FORCE_SUB_CHANNEL_2 and not FORCE_SUB_CHANNEL_3 and not FORCE_SUB_CHANNEL_REQUEST_1 and not FORCE_SUB_CHANNEL_REQUEST_2 and FORCE_SUB_CHANNEL_REQUEST_3:
        buttons = [
            [
                InlineKeyboardButton(text = "• عضویت اول", url = client.invitelink1)
            ],
            [
                InlineKeyboardButton(text = "• عضویت دوم", url = client.invitelink2)
            ],
            [
                InlineKeyboardButton(text = "• عضویت سوم", url = client.reinvitelink3)
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(text = "• عضو شدم | دانلود فایل", url = f"https://t.me/{client.username}?start={message.command[1]}")
                ]
            )
        except IndexError:
            pass
        return buttons
