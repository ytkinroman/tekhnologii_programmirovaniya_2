import asyncio
from time import perf_counter
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


async def sequence_async():
    start_time = perf_counter()

    await fibonacci(699998)
    await trapezoidal_rule(sin, 0, pi, 20000000)

    end_time = perf_counter()

    print(f"sequence_async time: {end_time - start_time: 0.2f} \n")


async def asyncio_gather_async():
    start_time = perf_counter()

    await asyncio.gather(
        fibonacci(699998),
        trapezoidal_rule(sin, 0, pi, 20000000)
    )

    end_time = perf_counter()

    print(f"asyncio_gather_async time: {end_time - start_time: 0.2f} \n")


def main():
    print("=" * 25)

    # Запуск асинхронных функций
    asyncio.run(sequence_async())
    asyncio.run(asyncio_gather_async())

    print("=" * 25)


if __name__ == "__main__":
    main()