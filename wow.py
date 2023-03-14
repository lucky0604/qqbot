from botpy import logging, BotAPI
from botpy.message import Message
from botpy.ext.command_util import Commands
from services.wow.achivements import get_mounts_collections
from services.wow.server_status import img_test

_log = logging.get_logger()


@Commands(name=("成就"))
async def get_achivement(api: BotAPI, message: Message, params=None):
    params_str_arr = params.split(" ")
    if params_str_arr[0] == "坐骑" or params_str_arr[0] == "mounts":
        result = get_mounts_collections(params_str_arr[1], params_str_arr[2])
        total = len(result["mounts"])
        await api.post_message(channel_id=message.channel_id,
                               content=f"您共有{total}个坐骑")
    return True

@Commands(name=("图片"))
async def get_img(api: BotAPI, message: Message, params=None):
    img_bytes = img_test()
    await api.post_message(channel_id=message.channel_id, file_image=img_bytes)
    return True