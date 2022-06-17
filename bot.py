#(©)Codexbotz

import pyromod.listen
from pyrogram import Client
import sys

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL_1, FORCE_SUB_CHANNEL_2, FORCE_SUB_CHANNEL_3, FORCE_SUB_CHANNEL_4, CHANNEL_ID, REQUEST_1, REQUEST_2, REQUEST_3, REQUEST_4

class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()

        if FORCE_SUB_CHANNEL_1:
            if REQUEST_1 == True:
                try:
                    link = (await self.create_chat_invite_link(FORCE_SUB_CHANNEL_1, creates_join_request = True)).invite_link
                    if not link:
                        await self.create_chat_invite_link(FORCE_SUB_CHANNEL_1, creates_join_request = True)
                        link = (await self.create_chat_invite_link(FORCE_SUB_CHANNEL_1, creates_join_request = True)).invite_link
                    self.invitelink1 = link
                except Exception as a:
                    self.LOGGER(__name__).warning(a)
                    self.LOGGER(__name__).warning("Bot can't Export Invite link from First Force Sub Channel!")
                    self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL_1 value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current First Force Sub Channel Value: {FORCE_SUB_CHANNEL_1}")
                    self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/CodeXBotzSupport for support")
                    sys.exit()
            elif REQUEST_1 == False:
                try:
                    link = (await self.get_chat(FORCE_SUB_CHANNEL_1)).invite_link
                    if not link:
                        await self.export_chat_invite_link(FORCE_SUB_CHANNEL_1)
                        link = (await self.get_chat(FORCE_SUB_CHANNEL_1)).invite_link
                    self.invitelink = link
                except Exception as a:
                    self.LOGGER(__name__).warning(a)
                    self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                    self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL}")
                    self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/CodeXBotzSupport for support")
                    sys.exit()

        if FORCE_SUB_CHANNEL_2:
            if REQUEST_2 == True:
                try:
                    link = (await self.create_chat_invite_link(FORCE_SUB_CHANNEL_2, creates_join_request = True)).invite_link
                    if not link:
                        await self.create_chat_invite_link(FORCE_SUB_CHANNEL_2, creates_join_request = True)
                        link = (await self.create_chat_invite_link(FORCE_SUB_CHANNEL_2, creates_join_request = True)).invite_link
                    self.invitelink1 = link
                except Exception as a:
                    self.LOGGER(__name__).warning(a)
                    self.LOGGER(__name__).warning("Bot can't Export Invite link from First Force Sub Channel!")
                    self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL_1 value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current First Force Sub Channel Value: {FORCE_SUB_CHANNEL_1}")
                    self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/CodeXBotzSupport for support")
                    sys.exit()
            elif REQUEST_2 == False:
                try:
                    link = (await self.get_chat(FORCE_SUB_CHANNEL_2)).invite_link
                    if not link:
                        await self.export_chat_invite_link(FORCE_SUB_CHANNEL_2)
                        link = (await self.get_chat(FORCE_SUB_CHANNEL_2)).invite_link
                    self.invitelink = link
                except Exception as a:
                    self.LOGGER(__name__).warning(a)
                    self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                    self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL}")
                    self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/CodeXBotzSupport for support")
                    sys.exit()

        if FORCE_SUB_CHANNEL_3:
            if REQUEST_3 == True:
                try:
                    link = (await self.create_chat_invite_link(FORCE_SUB_CHANNEL_3, creates_join_request = True)).invite_link
                    if not link:
                        await self.create_chat_invite_link(FORCE_SUB_CHANNEL_3, creates_join_request = True)
                        link = (await self.create_chat_invite_link(FORCE_SUB_CHANNEL_3, creates_join_request = True)).invite_link
                    self.invitelink1 = link
                except Exception as a:
                    self.LOGGER(__name__).warning(a)
                    self.LOGGER(__name__).warning("Bot can't Export Invite link from First Force Sub Channel!")
                    self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL_1 value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current First Force Sub Channel Value: {FORCE_SUB_CHANNEL_1}")
                    self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/CodeXBotzSupport for support")
                    sys.exit()
            elif REQUEST_3 == False:
                try:
                    link = (await self.get_chat(FORCE_SUB_CHANNEL_3)).invite_link
                    if not link:
                        await self.export_chat_invite_link(FORCE_SUB_CHANNEL_3)
                        link = (await self.get_chat(FORCE_SUB_CHANNEL_3)).invite_link
                    self.invitelink = link
                except Exception as a:
                    self.LOGGER(__name__).warning(a)
                    self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                    self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL}")
                    self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/CodeXBotzSupport for support")
                    sys.exit()

        if FORCE_SUB_CHANNEL_4:
            if REQUEST_4 == True:
                try:
                    link = (await self.create_chat_invite_link(FORCE_SUB_CHANNEL_4, creates_join_request = True)).invite_link
                    if not link:
                        await self.create_chat_invite_link(FORCE_SUB_CHANNEL_4, creates_join_request = True)
                        link = (await self.create_chat_invite_link(FORCE_SUB_CHANNEL_4, creates_join_request = True)).invite_link
                    self.invitelink1 = link
                except Exception as a:
                    self.LOGGER(__name__).warning(a)
                    self.LOGGER(__name__).warning("Bot can't Export Invite link from First Force Sub Channel!")
                    self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL_1 value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current First Force Sub Channel Value: {FORCE_SUB_CHANNEL_1}")
                    self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/CodeXBotzSupport for support")
                    sys.exit()
            elif REQUEST_4 == False:
                try:
                    link = (await self.get_chat(FORCE_SUB_CHANNEL_4)).invite_link
                    if not link:
                        await self.export_chat_invite_link(FORCE_SUB_CHANNEL_4)
                        link = (await self.get_chat(FORCE_SUB_CHANNEL_4)).invite_link
                    self.invitelink = link
                except Exception as a:
                    self.LOGGER(__name__).warning(a)
                    self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                    self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL}")
                    self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/CodeXBotzSupport for support")
                    sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/CodeXBotzSupport for support")
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by 𝘾𝙤𝙙𝙚 𝕏 𝘽𝙤𝙩𝙯\nhttps://t.me/CodeXBotz")
        self.username = usr_bot_me.username

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
