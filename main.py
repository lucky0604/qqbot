import uvicorn
from fastapi import FastAPI
import os
import botpy
from botpy.ext.cog_yaml import read
from robot import MyClient

app = FastAPI()
test_config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))


@app.on_event("startup")
async def startup_event():
    pass


@app.on_event("shutdown")
async def shutdown_event():
    pass


if __name__ == "__main__":
    intents = botpy.Intents(public_guild_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=test_config["token"]["appid"],
               token=test_config["token"]["token"])
    uvicorn.run(app="main:app", host="127.0.0.1", port=3000)