import os
import click
import uvicorn
from core.config import config, get_config_consts
import botpy
from botpy import logging
from botpy.message import Message

_log = logging.get_logger()
from wcl import wcl_robot
from wow import get_achivement, get_img
from core.config import get_config_consts
import asyncio
import threading

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


def init_robot() -> None:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    intents = botpy.Intents(public_guild_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=args["token"]["appid"], token=args["token"]["token"])


@click.command()
@click.option(
    "--env",
    type=click.Choice(["local", "dev", "prod"], case_sensitive=False),
    default="local",
)
@click.option(
    "--debug",
    type=click.BOOL,
    is_flag=True,
    default=False,
)
def main(env: str, debug: bool):
    os.environ["ENV"] = env
    os.environ["DEBUG"] = str(debug)

    uvicorn.run(
        app="backend.server:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=True if config.ENV != "production" else False,
        workers=2,
    )


t1 = threading.Thread(target=init_robot)

if __name__ == "__main__":
    t1.start()
    main()