import httpx
from utils.consts import WCL_URL, WCL_TOKEN


def getWclCharacterInfo(params):
    headers = {
        "Authorization": "Bearer " + WCL_TOKEN,
        "Content-Type": "application/json; charset=utf-8"
    }
    if params is None:
        return
    query_str = """query {{
        characterData{{
            character(name: "{0}", serverSlug: "{1}", serverRegion: "{2}") {{
                zoneRankings
            }}
        }}
    }}
    """.format(params["character_name"], params["server_name"],
               params["serverRegion"])
    jsonStr = {"query": query_str}
    with httpx.Client() as client:
        result = client.post(WCL_URL, json=jsonStr, headers=headers)
    return result.json()
