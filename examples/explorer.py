from env import load_env
import geoguessr_api
import asyncio

from models.enums import MapBrowseOption

username, password, token = load_env()


def sync_explorer():
    with geoguessr_api.Client(username, password, token) as client:
        print('--- Available countries on Geoguessr ---')
        all_countries = client.get_explorer()
        for country in all_countries:
            print('Name:', country.name, 'Code:', country.country_code)

        print('--- Explored countries ---')
        explored = client.get_explored_countries()
        for country in explored:
            print('Name:', country.name, 'Score:', country.best_score, 'Medal:', country.medal)

        print('--- Explored countries by user Lance ---')
        explored = client.get_explored_countries(user='5cf9e887b741f87ce8ce9759')  # str / User / UserMinified
        for country in explored:
            print('Name:', country.name, 'Score:', country.best_score, 'Medal:', country.medal)


async def async_explorer():
    async with geoguessr_api.AsyncClient(username, password, token) as client:
        print('--- Available countries on Geoguessr ---')
        all_countries = await client.get_explorer()
        for country in all_countries:
            print('Name:', country.name, '--- Code:', country.country_code)

        print('--- Explored countries ---')
        explored = await client.get_explored_countries()
        for country in explored:
            print('Name:', country.name, '--- Score:', country.best_score, '--- Medal:', country.medal)

        print('--- Explored countries by user Lance ---')
        explored = await client.get_explored_countries(user='5cf9e887b741f87ce8ce9759')  # str / User / UserMinified
        for country in explored:
            print('Name:', country.name, '--- Score:', country.best_score, '--- Medal:', country.medal)

if __name__ == '__main__':
    sync_explorer()
    asyncio.run(async_explorer())
