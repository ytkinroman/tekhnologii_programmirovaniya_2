import asyncio
from threading import Thread
from time import perf_counter
from multiprocessing import Process
from math import sin, pi


# Запускать с n=699998.
async def fibonacci(n: int) -> int:
    """Возвращает последнюю цифру n-е числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    print(f"fibonacci = {b % 10}")


# Запускать с f=math.sin, a=0, b=math.pi, n=20000000.
async def trapezoidal_rule(f, a, b, n):
    """Вычисляет определенный интеграл функции f от a до b методом трапеций с n шагами."""
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0

    for i in range(1, n):
        integral += f(a + i * h)

    print(f"trapezoidal_rule = {integral * h}")


async def sequence():
    start_time = perf_counter()

    await fibonacci(699998)
    await trapezoidal_rule(sin, 0, pi, 20000000)

    end_time = perf_counter()

    print(f"sequence time: {end_time - start_time: 0.2f} \n")


async def threads():
    start_time = perf_counter()

    loop = asyncio.get_event_loop()

    thread_fib = Thread(target=loop.run_until_complete, args=(fibonacci(699998),))
    thread_trap = Thread(target=loop.run_until_complete, args=(trapezoidal_rule(sin, 0, pi, 20000000),))

    thread_fib.start()  # Запуск потока.
    thread_trap.start()

    thread_fib.join()  # Ожидание завершения потока.
    thread_trap.join()

    end_time = perf_counter()

    print(f"threads time: {end_time - start_time: 0.2f} \n")


async def processes():
    start_time = perf_counter()

    loop = asyncio.get_event_loop()

    process_fib = Process(target=loop.run_until_complete, args=(fibonacci(699998),))
    process_trap = Process(target=loop.run_until_complete, args=(trapezoidal_rule(sin, 0, pi, 20000000),))

    process_fib.start()
    process_trap.start()

    process_fib.join()
    process_trap.join()

    end_time = perf_counter()

    print(f"processes time: {end_time - start_time: 0.2f} \n")


async def main():
    print("=" * 25)

    # await sequence()
    # await threads()
    await processes()

    print("=" * 25)


if __name__ == "__main__":
    asyncio.run(main())
