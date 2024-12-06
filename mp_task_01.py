from threading import Thread
from time import perf_counter
from multiprocessing import Process
import requests  # pip install requests
from typing import List


def fetch_url(url: str) -> str:
    """Получает содержимое веб-страницы."""
    response = requests.get(url)
    return response.text


def sequence(urls: List[str]) -> None:
    """Последовательно получает содержимое веб-страниц."""
    start_time = perf_counter()

    for url in urls:
        fetch_url(url)  # Запрос.

    end_time = perf_counter()

    print(f"\n    sequence time: {end_time - start_time: 0.2f} sec.\n")


def threads(urls: List[str]) -> None:
    """С помощью потоков получает содержимое веб-страниц."""
    start_time = perf_counter()

    threads_list = []
    for url in urls:
        thread = Thread(target=fetch_url, args=(url,))  # Аргумент - это картёж.
        threads_list.append(thread)

    for thread in threads_list:
        thread.start()  # Запуск потока.

    for thread in threads_list:
        thread.join()  # Ожидание завершения потока.

    end_time = perf_counter()

    print(f"    threads time: {end_time - start_time: 0.2f} sec.\n")


def processes(urls: List[str]) -> None:
    """С помощью процессов получает содержимое веб-страниц."""
    start_time = perf_counter()

    processes_list = []
    for url in urls:
        process = Process(target=fetch_url, args=(url,))
        processes_list.append(process)

    for process in processes_list:
        process.start()

    for process in processes_list:
        process.join()

    end_time = perf_counter()

    print(f"    processes time: {end_time - start_time: 0.2f} sec.\n")


def main() -> None:
    # Википедия по существующим в мире эстетикам xdd
    urls = ["https://aesthetics.fandom.com/wiki/Aesthetics_Wiki"] * 10

    print("=" * 40)

    # sequence(urls)   # Последовательно.
    # threads(urls)    # Потоки.
    processes(urls)  # Процессы.

    print("=" * 40)


if __name__ == "__main__":
    main()
