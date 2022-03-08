from env import load_env
import geoguessr_api
import asyncio

from geoguessr_api import BadRequest

username, password, token = load_env()


def sync_friend_request():
    with geoguessr_api.Client(username, password, token) as client:
        # Get friend requests
        pending_requests = client.pending_friend_requests()
        # Accept a friend request
        if pending_requests:
            user = pending_requests.pop(0)
            client.accept_friend(user)
        # List friends
        friends = client.list_friends(count=20, page=0)
        # Remove friends
        no_longer_friend = friends[0]
        client.remove_friend(no_longer_friend)
        # Add friends
        try:
            client.add_friend('5c3200a4dfdaaa1a24326a78')  # Accepts an id string, User or UserMinified as argument
            client.add_friend('5c3200a4')  # Invalid id string
        except BadRequest as error:  # If id string is invalid or user already has a pending request from you
            print(error.message)


async def async_friend_request():
    async with geoguessr_api.AsyncClient(username, password, token) as client:
        # Get friend requests
        pending_requests = await client.pending_friend_requests()
        # Accept a friend request
        if pending_requests:
            user = pending_requests.pop(0)
            await client.accept_friend(user)
        # List friends
        friends = await client.list_friends(count=20, page=0)
        # Remove friends
        no_longer_friend = friends[0]
        await client.remove_friend(no_longer_friend)
        # Add friends
        try:
            await client.add_friend('5c3200a4dfdaaa1a24326a78') # Accepts an id string, User or UserMinified as argument
            await client.add_friend('5c3200a4')  # Invalid id string
        except BadRequest as error:  # If id string is invalid or user already has a pending request from you
            print(error.message)


if __name__ == '__main__':
    sync_friend_request()
    asyncio.run(async_friend_request())
