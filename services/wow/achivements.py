from utils.battlenet_token import get_battlenet_token
from utils.consts import BATTLENET_URL
import httpx


def get_mounts_collections(realmSlug, characterName):
    token = get_battlenet_token()
    params = {"namespace": "profile-us"}
    headers = {"Authorization": "Bearer " + token}
    result = httpx.get(
        BATTLENET_URL +
        "/profile/wow/character/{0}/{1}/collections/mounts".format(
            realmSlug, characterName),
        headers=headers,
        params=params)
    print(
        BATTLENET_URL +
        "/profile/wow/character/{0}/{1}/collections/mounts".format(
            realmSlug, characterName),
        " ============= request url ===============")
    return result.json()
