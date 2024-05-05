import asyncio
import aiofiles


async def process_file(file_name):
    async with aiofiles.open(file_name, mode='r', encoding='utf-8') as file:
        num_lines = 0
        async for _ in file:
            num_lines += 1
        print(f"Number of lines in {file_name}: {num_lines}")


async def main():
    files = ['wiki.txt', 'Корпоративные ценности.txt', 'test.txt']
    tasks = [process_file(file) for file in files]

    await asyncio.gather(*tasks)


asyncio.run(main())
