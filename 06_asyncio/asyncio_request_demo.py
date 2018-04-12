import asyncio
import time
import requests

from aiohttp import ClientSession


async def make_asyncio_request(url, index, session):
    async with session.get(url) as response:
        return index


async def make_asyncio_requests(max, url):
    print('Asyncio requests')
    start_time = time.time()

    async with ClientSession() as session:
        tasks = [
            make_asyncio_request(url, index, session)
            for index in range(0, max)
        ]
        responses = await asyncio.gather(*tasks)

    print(responses)
    execution_time = time.time() - start_time
    print(f'execution time: {execution_time}s')


def make_sync_requests(max, url):
    print('Sync requests')
    start_time = time.time()

    response = []
    for i in range(0, max):
        requests.get(url)
        response.append(i)

    print(response)
    execution_time = time.time() - start_time
    print(f'execution time: {execution_time}s')


# Test it!

max = 10
url = 'http://httpbin.org/delay/1'

print('=========================================')

loop = asyncio.get_event_loop()
loop.run_until_complete(make_asyncio_requests(max, url))

print('-----------------------------------------')
make_sync_requests(max, url)

print('-----------------------------------------')
