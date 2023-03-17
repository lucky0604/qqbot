import os
import click
import uvicorn
from core.config import config, get_config_consts
import botpy
from robot import MyClient
from core.config import get_config_consts
import asyncio
import threading

args = get_config_consts()


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