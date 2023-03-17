import httpx
from utils.redis_util import get_redis
from utils.consts import BATTLENET_TOKEN_URL
from core.config import get_config_consts


def get_battlenet_token():
    args = get_config_consts()
    redis_client = get_redis()
    token = redis_client.get("battlenet_token")
    if token is None:
        params = {"grant_type": "client_credentials"}
        with httpx.Client() as client:
            result = client.post(BATTLENET_TOKEN_URL,
                                 params=params,
                                 auth=(args["battlenet"]["appid"],
                                       args["battlenet"]["appsecret"]))
            if result.json() is not None:
                redis_client.set("battlenet_token",
                                 result.json()["access_token"],
                                 ex=result.json()["expires_in"])
    return token
