import threading
import time
import multiprocessing
import math
import requests

# список url
urls = ['https://www.example.com'] * 10


def fetch_url(url):
    response = requests.get(url)
    return response.text


def sequence():
    # время старта start_time
    # выполнение функции fetch_url для каждого url из urls
    # время окончания end_time
    print(f'sequence time: {end_time - start_time: 0.2f} \n')


def threads():
    # время старта start_time
    # выполнение с помощью потоков функции fetch_url для каждого url из urls (с ожиданием окончания выполнения всех потоков)
    # время окончания end_time
    print(f'threads time: {end_time - start_time: 0.2f} \n')


def processes():
    # время старта start_time
    # выполнение с помощью процессов функции fetch_url для каждого url из urls (с ожиданием окончания выполнения всех процессов)
    # время окончания end_time
    print(f'processes time: {end_time - start_time: 0.2f} \n')


if __name__ == '__main__':
    sequence()
    threads()
    processes()
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):
        
        sequence time:  ???

        threads time:  ???
        
        processes time:  ???
    """
