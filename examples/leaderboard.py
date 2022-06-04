from env import load_env
import geoguessr_api
import asyncio

from models.enums import LeaderboardType

username, password, token = load_env()


def sync_leaderboard():
    with geoguessr_api.Client(username, password, token) as client:
        print("==== GLOBAL LEADERBOARD ====")
        leaderboard = client.get_leaderboard()
        for user in leaderboard:
            print(user.position, '-', user.nick, '|', user.rating)
        print("==== PERSONAL LEADERBOARD ====")
        leaderboard = client.get_leaderboard(type=LeaderboardType.CLIENT)
        for user in leaderboard:
            print(user.position, '-', user.nick, '|', user.rating)
        print("==== FRIEND LEADERBOARD ====")
        leaderboard = client.get_leaderboard(type=LeaderboardType.FRIENDS)
        for user in leaderboard:
            print(user.position, '-', user.nick, '|', user.rating)

async def async_leaderboard():
    async with geoguessr_api.AsyncClient(username, password, token) as client:
        print("==== GLOBAL LEADERBOARD ====")
        leaderboard = await client.get_leaderboard()
        for user in leaderboard:
            print(user.position, '-', user.nick, '|', user.rating)
        print("==== PERSONAL LEADERBOARD ====")
        leaderboard = await client.get_leaderboard(type=LeaderboardType.CLIENT)
        for user in leaderboard:
            print(user.position, '-', user.nick, '|', user.rating)
        print("==== FRIEND LEADERBOARD ====")
        leaderboard = await client.get_leaderboard(type=LeaderboardType.FRIENDS)
        for user in leaderboard:
            print(user.position, '-', user.nick, '|', user.rating)



if __name__ == '__main__':
    sync_leaderboard()
    asyncio.run(async_leaderboard())
