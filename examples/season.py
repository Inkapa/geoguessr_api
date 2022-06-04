from env import load_env
import geoguessr_api
import asyncio

from models.enums import LeaderboardType, SeasonType

username, password, token = load_env()


def sync_season():
    with geoguessr_api.Client(username, password, token) as client:
        current_season = client.get_season()
        previous_season = client.get_season(type=SeasonType.PREVIOUS)

        print("Current season:", current_season.name)
        print("Previous season:", previous_season.name)

        print(f"==== {current_season.name} LEADERBOARD ====")
        leaderboard = client.get_season_leaderboard(current_season)
        for user in leaderboard:
            print(user.position, '-', user.nick, '|', user.points)
        print(f"==== {previous_season.name} LEADERBOARD ====")
        leaderboard = client.get_season_leaderboard(current_season)
        for user in leaderboard:
            print(user.position, '-', user.nick, '|', user.points)


async def async_season():
    async with geoguessr_api.AsyncClient(username, password, token) as client:
        current_season = await client.get_season()
        previous_season = await client.get_season(type=SeasonType.PREVIOUS)

        print("Current season:", current_season.name)
        print("Previous season:", previous_season.name)

        print(f"==== {current_season.name} LEADERBOARD ====")
        leaderboard = await client.get_season_leaderboard(current_season)
        for user in leaderboard:
            print(user.position, '-', user.nick, '|', user.points)
        print(f"==== {previous_season.name} LEADERBOARD ====")
        leaderboard = await client.get_season_leaderboard(current_season)
        for user in leaderboard:
            print(user.position, '-', user.nick, '|', user.points)


if __name__ == '__main__':
    sync_season()
    asyncio.run(async_season())
