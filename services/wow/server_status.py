from utils.battlenet_token import get_battlenet_token
from utils.consts import BATTLENET_URL
import httpx

def img_test():
    with open("1.png", "rb") as img:
        img_bytes = img.read()
    return img_bytes