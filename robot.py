""" basic sample
import botpy
from botpy.message import Message

class MyClient(botpy.Client):
    async def on_at_message_create(self, message: Message):
        await message.reply(content=f"机器人{self.robot.name}收到你的消息了: {message.content}")

intents = botpy.Intents(public_guild_messages=True)
client = MyClient(intents=intents)
client.run(appid="102044184", token="JA3H4mGmvp3urHREg9Ori9zstXZMjYQF")
"""
import asyncio
import os
import botpy
from botpy import logging, BotAPI
from botpy.ext.cog_yaml import read
from botpy.message import Message
from botpy.ext.command_util import Commands

_log = logging.get_logger()
from wcl import wcl_robot
from wow import get_achivement, get_img
from core.config import get_config_consts

args = get_config_consts()


class MyClient(botpy.Client):

    async def on_ready(self):
        # members = await self.api.get_guild_members(guild_id="pkcani395b")
        # _log.info(members, " ======= mmbers ==========")
        _log.info(f"robot [{self.robot.name}] on ready")

    async def on_at_message_create(self, message: Message):
        member = await self.api.get_guild_member(guild_id=message.guild_id,
                                                 user_id=message.author.id)
        print(member, " ========== member ===========")
        handlers = [wcl_robot, get_achivement, get_img]
        for handler in handlers:
            if await handler(api=self.api, message=message):
                return
