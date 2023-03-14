from botpy import logging, BotAPI
from botpy.message import Message
from botpy.ext.command_util import Commands
import zhconv
from services.wcl.wcl_info import getWclCharacterInfo

_log = logging.get_logger()


@Commands(name=("WCL", "wcl"))
async def wcl_robot(api: BotAPI, message: Message, params=None):
    # _log.info(params)
    _log.info(params.split(" "))
    str_arr = params.split(" ")
    str_after = []
    for i in str_arr:
        i = zhconv.convert(i, "zh-hant")
        i = zhconv.convert(i, "zh-tw")
        str_after.append(i)
    if ["台服", "臺服", "亚服", "亞服", "tw", "TW"].index(str_after[1]) != -1:
        str_after[1] = "TW"
    params = {
        "character_name": str_after[0],
        "serverRegion": str_after[1],
        "server_name": str_after[2]
    }
    _log.info(params)
    result = getWclCharacterInfo(params)
    content = ""
    if len(result["data"]["characterData"]["character"]["zoneRankings"]
           ["allStars"]) == 0:
        content = "您还没有当前版本的WCL分数，快去努力战斗吧！"
    else:
        for i in result["data"]["characterData"]["character"]["zoneRankings"][
                "allStars"]:
            content += "您的" + str(i["spec"]) + "天赋分数为：" + str(
                i["points"]) + "\n" + "区域排名为: " + str(
                    i["regionRank"]) + "\n" + "服务器排名为: " + str(i["serverRank"])
    await api.post_message(channel_id=message.channel_id,
                           content=content,
                           msg_id=message.id)
    return True