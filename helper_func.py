#(©)Codexbotz

import base64
import re
import asyncio
from pyrogram import filters
from config import FORCE_SUB_CHANNEL_1, FORCE_SUB_CHANNEL_2, FORCE_SUB_CHANNEL_3, FORCE_SUB_CHANNEL_4, ADMINS
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors import FloodWait

async def is_subch1(filter, client, update):
    if not FORCE_SUB_CHANNEL_1:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL_1, user_id = user_id)
    except UserNotParticipant:
        return False

    if not member.status in ["creator", "administrator", "member"]:
        return False
    else:
        return True

async def is_subch2(filter, client, update):
    if not FORCE_SUB_CHANNEL_2:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL_2, user_id = user_id)
    except UserNotParticipant:
        return False

    if not member.status in ["creator", "administrator", "member"]:
        return False
    else:
        return True

async def is_subch3(filter, client, update):
    if not FORCE_SUB_CHANNEL_3:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL_3, user_id = user_id)
    except UserNotParticipant:
        return False

    if not member.status in ["creator", "administrator", "member"]:
        return False
    else:
        return True

async def is_subch4(filter, client, update):
    if not FORCE_SUB_CHANNEL_4:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL_4, user_id = user_id)
    except UserNotParticipant:
        return False

    if not member.status in ["creator", "administrator", "member"]:
        return False
    else:
        return True

async def is_subscribed(filter, client, update):
    if not FORCE_SUB_CHANNEL_1:
        return True
    if not FORCE_SUB_CHANNEL_2:
        return True
    if not FORCE_SUB_CHANNEL_3:
        return True
    if not FORCE_SUB_CHANNEL_4:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL_1, user_id = user_id)
    except UserNotParticipant:
        return False
    try:
        member = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL_2, user_id = user_id)
    except UserNotParticipant:
        return False
    try:
        member = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL_3, user_id = user_id)
    except UserNotParticipant:
        return False
    try:
        member = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL_4, user_id = user_id)
    except UserNotParticipant:
        return False

    if not member.status in ["creator", "administrator", "member"]:
        return False
    else:
        return True

async def convert(text: str) -> str:
    table = str.maketrans({
        "1": "4",
        "2": "0",
        "3": "8",
        "4": "2",
        "5": "6",
        "6": "1",
        "7": "9",
        "8": "5",
        "9": "3",
        "0": "7",
    })
    return text.translate(table)

async def reconvert(text: str) -> str:
    retable = str.maketrans({
        "4": "1",
        "0": "2",
        "8": "3",
        "2": "4",
        "6": "5",
        "1": "6",
        "9": "7",
        "5": "8",
        "3": "9",
        "7": "0",
    })
    return text.translate(retable)

async def encode(string):
    string_bytes = string.encode("ascii")
    string_convert = convert(string_bytes)
    base64_bytes = base64.urlsafe_b64encode(string_convert)
    base64_string = (base64_bytes.decode("ascii")).strip("=")
    return base64_string

async def decode(base64_string):
    base64_string = base64_string.strip("=") # links generated before this commit will be having = sign, hence striping them to handle padding errors.
    base64_bytes = (base64_string + "=" * (-len(base64_string) % 4)).encode("ascii")
    string_bytes = base64.urlsafe_b64decode(base64_bytes) 
    string_reconvert = reconvert(string_bytes) 
    string = string_reconvert.decode("ascii")
    return string

async def get_messages(client, message_ids):
    messages = []
    total_messages = 0
    while total_messages != len(message_ids):
        temb_ids = message_ids[total_messages:total_messages+200]
        try:
            msgs = await client.get_messages(
                chat_id=client.db_channel.id,
                message_ids=temb_ids
            )
        except FloodWait as e:
            await asyncio.sleep(e.x)
            msgs = await client.get_messages(
                chat_id=client.db_channel.id,
                message_ids=temb_ids
            )
        except:
            pass
        total_messages += len(temb_ids)
        messages.extend(msgs)
    return messages

async def get_message_id(client, message):
    if message.forward_from_chat:
        if message.forward_from_chat.id == client.db_channel.id:
            return message.forward_from_message_id
        else:
            return 0
    elif message.forward_sender_name:
        return 0
    elif message.text:
        pattern = "https://t.me/(?:c/)?(.*)/(\d+)"
        matches = re.match(pattern,message.text)
        if not matches:
            return 0
        channel_id = matches.group(1)
        msg_id = int(matches.group(2))
        if channel_id.isdigit():
            if f"-100{channel_id}" == str(client.db_channel.id):
                return msg_id
        else:
            if channel_id == client.db_channel.username:
                return msg_id
    else:
        return 0

subch1 = filters.create(is_subch1)
subch2 = filters.create(is_subch2)
subch3 = filters.create(is_subch3)
subch4 = filters.create(is_subch4)
subscribed = filters.create(is_subscribed)
