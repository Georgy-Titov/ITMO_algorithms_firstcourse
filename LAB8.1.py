import asyncio
import aiohttp


async def fetch_content(url, session):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = [
        'https://itmo.ru',
        'https://yandex.ru',
        'https://www.google.com'
    ]
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in urls:
            task = asyncio.create_task(fetch_content(i, session))
            tasks.append(task)

        results = await asyncio.gather(*tasks)

        for url, page in zip(urls, results):
            print(f"Page from {url}:\n\tText length: {len(page)}")


asyncio.run(main())
