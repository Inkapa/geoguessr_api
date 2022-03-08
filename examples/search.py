import random

from env import load_env
import geoguessr_api
import asyncio

from models.enums import SearchOption
from models.maps.search import SearchMap

username, password, token = load_env()


def sync_search():
    with geoguessr_api.Client(username, password, token) as client:
        for search_type in SearchOption:
            search = client.search(query='Yellow', search_type=search_type, count=3)
            yellow = random.choice(search)
            if isinstance(yellow, SearchMap):
                highscore = client.get_map_highscores(yellow)
                print(f"Ranked first in map '{yellow.name}':", highscore.all[0].nick)
            else:
                user = client.get_user(yellow)  # Get full User object through UserMinified object or through id as str
                print(f"{yellow.nick}'s BR level:", user.br.level)


async def async_search():
    async with geoguessr_api.AsyncClient(username, password, token) as client:
        for search_type in SearchOption:
            search = await client.search(query='Yellow', search_type=search_type, count=3)
            yellow = random.choice(search)
            if isinstance(yellow, SearchMap):
                highscore = await client.get_map_highscores(yellow)
                print(f"Ranked first in map '{yellow.name}':", highscore.all[0].nick)
            else:
                user = await client.get_user(yellow)
                print(f"{yellow.nick}'s BR level:", user.br.level)


if __name__ == '__main__':
    sync_search()
    asyncio.run(async_search())
