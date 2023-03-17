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
        _log.info(f"robot [{self.robot.name}] on ready")

    async def on_at_message_create(self, message: Message):
        # str_after = message.content.split(" ")
        # params = {
        #     "character_name": str_after[1],
        #     "serverRegion": str_after[2],
        #     "server_name": str_after[3]
        # }
        # result = getWclCharacterInfo(params)
        # await self.api.post_message(channel_id=message.channel_id, content=str(result))
        handlers = [wcl_robot, get_achivement, get_img]
        for handler in handlers:
            if await handler(api=self.api, message=message):
                return


if __name__ == "__main__":
    print(args["token"]["appid"])
    intents = botpy.Intents(public_guild_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=args["token"]["appid"], token=args["token"]["token"])
