import asyncio
import aiohttp  # pip install aiohttp
from time import perf_counter
from typing import List


async def fetch_url(session: aiohttp.ClientSession, url: str) -> str:
    """Асинхронно получает содержимое веб-страницы."""
    async with session.get(url) as response:
        return await response.text()


async def sequence_async(urls: List[str]) -> None:
    """Асинхронно последовательно получает содержимое веб-страниц."""
    start_time = perf_counter()

    async with aiohttp.ClientSession() as session:
        for url in urls:
            await fetch_url(session, url)  # Асинхронный запрос.

    end_time = perf_counter()

    print(f"\n    sequence_async time: {end_time - start_time: 0.2f} sec.\n")


async def asyncio_gather(urls: List[str]) -> None:
    """Асинхронно получает содержимое веб-страниц с использованием asyncio.gather."""
    start_time = perf_counter()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)

    end_time = perf_counter()

    print(f"    asyncio_gather time: {end_time - start_time: 0.2f} sec.\n")


def main() -> None:
    # Википедия по существующим в мире эстетикам xdd
    urls = ["https://aesthetics.fandom.com/wiki/Aesthetics_Wiki"] * 100

    print("=" * 40)

    # Запуск асинхронных функций
    asyncio.run(sequence_async(urls))  # Асинхронно последовательно.
    # asyncio.run(asyncio_gather(urls))  # Асинхронно параллельно.

    print("=" * 40)


if __name__ == "__main__":
    main()