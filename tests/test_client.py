import geoguessr_api
import asyncio
from examples.env import load_env

username, password, token = load_env()


def test_sync_client():
    with geoguessr_api.Client(username, password, token) as client:
        assert client.token == token
        assert client.me.email.address == username


async def test_async_client():
    async with geoguessr_api.AsyncClient(username, password, token) as client:
        assert client.token == token
        assert client.me.email.address == username

if __name__ == '__main__':
    test_sync_client()
    asyncio.run(test_async_client())
