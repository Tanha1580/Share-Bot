#(©)Codexbotz

import base64
import re
import asyncio
from pyrogram import filters
from config import FORCE_SUB_CHANNEL, ADMINS
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors import FloodWait

async def is_subscribed(filter, client, update):
    if not FORCE_SUB_CHANNEL:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id = FORCE_SUB_CHANNEL, user_id = user_id)
    except UserNotParticipant:
        return False

    if not member.status in ["creator", "administrator", "member"]:
        return False
    else:
        return True

async def convert(textt: str) -> str:
    table = str.maketrans({
        "A": "G", "B": "U",
        "C": "M", "D": "V",
        "E": "B", "F": "P",
        "G": "Q", "H": "E",
        "I": "L", "J": "R",
        "K": "J", "L": "X",
        "M": "H", "N": "I",
        "O": "T", "P": "N",
        "Q": "C", "R": "O",
        "S": "A", "T": "F",
        "U": "Y", "V": "D",
        "W": "Z", "X": "K",
        "Y": "W", "Z": "S",
        "0": "4", "1": "6",
        "2": "3", "3": "7",
        "4": "0", "5": "8",
        "6": "1", "7": "9",
        "8": "2", "9": "5"
    })
    return textt.translate(table)

async def reconvert(ttext: str) -> str:
    table = str.maketrans({
        "G": "A", "U": "B",
        "M": "C", "V": "D",
        "B": "E", "P": "F",
        "Q": "G", "E": "H",
        "L": "I", "R": "J",
        "J": "K", "X": "L",
        "H": "M", "I": "N",
        "T": "O", "N": "P",
        "C": "Q", "O": "R",
        "A": "S", "F": "T",
        "Y": "U", "D": "V",
        "Z": "W", "K": "X",
        "W": "Y", "S": "Z",
        "4": "0", "6": "1",
        "3": "2", "7": "3",
        "0": "4", "8": "5",
        "1": "6", "9": "7",
        "2": "8", "5": "9"
    })
    return ttext.translate(table)

async def encode(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.urlsafe_b64encode(string_bytes)
    base64_string = (base64_bytes.decode("ascii")).strip("=")
    return base64_string

async def decode(base64_string):
    base64_string = base64_string.strip("=") # links generated before this commit will be having = sign, hence striping them to handle padding errors.
    base64_bytes = (base64_string + "=" * (-len(base64_string) % 4)).encode("ascii")
    string_bytes = base64.urlsafe_b64decode(base64_bytes) 
    string = string_bytes.decode("ascii")
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

subscribed = filters.create(is_subscribed)
