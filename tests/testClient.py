import geoguessr_api
import asyncio
from dotenv import load_dotenv
import os
load_dotenv()
username = os.getenv('GEO_USERNAME')
password = os.getenv('GEO_PASSWORD')

def testSyncClient():
    with geoguessr_api.Client(username, password) as client:
        print(client)

async def testAsyncClient():
    async with geoguessr_api.AsyncClient(username, password) as client:
        print(client.me)
        print('Division BR:', client.me.br.division)
        print('Level BR:', client.me.br.level)

if __name__ == '__main__':
    testSyncClient()
    asyncio.run(testAsyncClient())
