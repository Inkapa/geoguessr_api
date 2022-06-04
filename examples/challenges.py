from env import load_env
import geoguessr_api
import asyncio

from models.enums import LeaderboardType, SeasonType

username, password, token = load_env()


def sync_challenges():
    with geoguessr_api.Client(username, password, token) as client:
        uk = client.get_explorer('uk')
        print("Map: ", uk.name)
        challenge = client.create_challenge(uk, zooming=False)
        print("Challenge url: ", f"https://www.geoguessr.com/challenge/{challenge.token}")


async def async_challenges():
    async with geoguessr_api.AsyncClient(username, password, token) as client:
        uk = await client.get_explorer('uk')
        print("Map: ", uk.name)
        challenge = await client.create_challenge(uk, zooming=False)
        print("Challenge url: ", f"https://www.geoguessr.com/challenge/{challenge.token}")

if __name__ == '__main__':
    sync_challenges()
    asyncio.run(async_challenges())
