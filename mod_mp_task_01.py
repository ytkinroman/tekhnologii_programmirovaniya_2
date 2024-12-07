import asyncio
import aiohttp
from threading import Thread
from multiprocessing import Process
from time import perf_counter
from typing import List


async def fetch_url(session: aiohttp.ClientSession, url: str) -> str:
    """Асинхронно получает содержимое веб-страницы."""
    async with session.get(url) as response:
        return await response.text()


def fetch_url_sync(url: str) -> str:
    """Для вызова асинхронной функции fetch_url."""
    return asyncio.run(fetch_url_async(url))


async def fetch_url_async(url: str) -> str:
    """Асинхронная функция для получения содержимого веб-страницы."""
    async with aiohttp.ClientSession() as session:
        return await fetch_url(session, url)


def sequence(urls: List[str]) -> None:
    """Последовательно получает содержимое веб-страниц."""
    start_time = perf_counter()

    for url in urls:
        fetch_url_sync(url)  # Запрос.

    end_time = perf_counter()

    print(f"\n  sequence time: {end_time - start_time: 0.2f} sec.\n")


def threads(urls: List[str]) -> None:
    """С помощью потоков получает содержимое веб-страниц."""
    start_time = perf_counter()

    threads_list = []
    for url in urls:
        thread = Thread(target=fetch_url_sync, args=(url,))  # Аргумент - это картёж.
        threads_list.append(thread)

    for thread in threads_list:
        thread.start()  # Запуск потока.

    for thread in threads_list:
        thread.join()  # Ожидание завершения потока.

    end_time = perf_counter()

    print(f"  threads time: {end_time - start_time: 0.2f} sec.\n")


def processes(urls: List[str]) -> None:
    """С помощью процессов получает содержимое веб-страниц."""
    start_time = perf_counter()

    processes_list = []
    for url in urls:
        process = Process(target=fetch_url_sync, args=(url,))
        processes_list.append(process)

    for process in processes_list:
        process.start()

    for process in processes_list:
        process.join()

    end_time = perf_counter()

    print(f"  processes time: {end_time - start_time: 0.2f} sec.\n")


def main() -> None:
    # Википедия по существующим в мире эстетикам xdd
    urls = ["https://aesthetics.fandom.com/wiki/Aesthetics_Wiki"] * 100

    print("=" * 25)

    # sequence(urls)   # Последовательно.
    # threads(urls)    # Потоки.
    processes(urls)  # Процессы.

    print("=" * 25)


if __name__ == "__main__":
    main()
