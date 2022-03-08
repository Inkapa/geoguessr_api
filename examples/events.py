import random

from env import load_env
import geoguessr_api
import asyncio

username, password, token = load_env()


def sync_events():
    with geoguessr_api.Client(username, password, token) as client:
        competitions = client.get_events()
        competition = random.choice(competitions)
        print(competition.name, '|', competition.description)
        results = client.get_event_results(competition)   # id str / Event object
        print('Position: ', results.position)


async def async_events():
    async with geoguessr_api.AsyncClient(username, password, token) as client:
        competitions = await client.get_events()
        competition = random.choice(competitions)
        print(competition.name, '|', competition.description)
        results = await client.get_event_results(competition)   # id str / Event object
        print('Position: ', results.position)


if __name__ == '__main__':
    sync_events()
    asyncio.run(async_events())
