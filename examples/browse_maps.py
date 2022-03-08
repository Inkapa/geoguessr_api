import random

from env import load_env
import geoguessr_api
import asyncio

from models.enums import MapBrowseOption

username, password, token = load_env()


def sync_browse_maps():
    with geoguessr_api.Client(username, password, token) as client:
        perso_map = client.browse_maps()
        client.like_map(perso_map)  # id as str, SearchMap and Map objects are accepted
        assert client.is_map_liked(perso_map)
        recommended_maps = client.browse_maps(reference_map_id=perso_map, count=5, page=0)
        for recommended_map in recommended_maps:
            print(f'RECOMMENDED BASED ON MAP {perso_map.name}:', recommended_map.name)
        browse_types = (option for option in MapBrowseOption if option != MapBrowseOption.PERSONALIZED)
        for map_type in browse_types:
            random_map = client.browse_maps(browse_type=map_type, count=3)
            print(f"{map_type}:", random.choice(random_map).name)
        maps_by_user = client.browse_maps_by_user(user='5bd2cd241f3cf81af80e02ba')  # id str, User or UserMinified
        print('Map created by ttv/kizawski:', random.choice(maps_by_user).name)


async def async_browse_maps():
    async with geoguessr_api.AsyncClient(username, password, token) as client:
        perso_map = await client.browse_maps()
        await client.like_map(perso_map)
        assert await client.is_map_liked(perso_map)
        recommended_maps = await client.browse_maps(reference_map_id=perso_map, count=5, page=0)
        for recommended_map in recommended_maps:
            print(f'RECOMMENDED BASED ON MAP {perso_map.name}:', recommended_map.name)
        browse_types = (option for option in MapBrowseOption if option != MapBrowseOption.PERSONALIZED)
        for map_type in browse_types:
            random_map = await client.browse_maps(browse_type=map_type, count=3)
            print(f"{map_type}:", random.choice(random_map).name)
        maps_by_user = await client.browse_maps_by_user(user='5bd2cd241f3cf81af80e02ba')  # id str, User or UserMinified
        print('Map created by ttv/kizawski:', random.choice(maps_by_user).name)

if __name__ == '__main__':
    sync_browse_maps()
    asyncio.run(async_browse_maps())
