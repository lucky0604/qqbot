import httpx
from utils.redis_util import get_redis
from utils.consts import APP_ID, APP_SECRET, BATTLENET_TOKEN_URL


def get_battlenet_token():
    redis_client = get_redis()
    token = redis_client.get("battlenet_token")
    if token is None:
        params = {"grant_type": "client_credentials"}
        with httpx.Client() as client:
            result = client.post(BATTLENET_TOKEN_URL,
                                 params=params,
                                 auth=(APP_ID, APP_SECRET))
            if result.json() is not None:
                redis_client.set("battlenet_token",
                                 result.json()["access_token"],
                                 ex=result.json()["expires_in"])
    return token
