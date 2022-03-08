import geoguessr_api
import asyncio
from examples.env import load_env
from models.enums import FriendStatus

username, password, token = load_env()


def test_sync_friends():
    with geoguessr_api.Client(username, password, token) as client:
        assert client.friendship_status('604bca0a8c4d150001e73dc4') == FriendStatus.NOT_FRIENDS
        client.add_friend('604bca0a8c4d150001e73dc4')
        assert client.friendship_status('604bca0a8c4d150001e73dc4') == FriendStatus.REQUEST_SENT
        client.remove_friend('604bca0a8c4d150001e73dc4')
        assert client.friendship_status('604bca0a8c4d150001e73dc4') == FriendStatus.NOT_FRIENDS

async def test_async_friends():
    async with geoguessr_api.AsyncClient(username, password, token) as client:
        assert await client.friendship_status('604bca0a8c4d150001e73dc4') == FriendStatus.NOT_FRIENDS
        await client.add_friend('604bca0a8c4d150001e73dc4')
        assert await client.friendship_status('604bca0a8c4d150001e73dc4') == FriendStatus.REQUEST_SENT
        await client.remove_friend('604bca0a8c4d150001e73dc4')
        assert await client.friendship_status('604bca0a8c4d150001e73dc4') == FriendStatus.NOT_FRIENDS

if __name__ == '__main__':
    test_sync_friends()
    asyncio.run(test_async_friends())
