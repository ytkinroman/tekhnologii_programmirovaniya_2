import threading
import time
import multiprocessing
import math

# Функции для АТ-04

# запускать с n = 699998
def fibonacci(n):  # содержимое функции не менять
    """Возвращает последнюю цифру n-е числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(f'fibonacci = {b % 10}')


# запускать с f, a, b, n равными соответственно math.sin, 0, math.pi, 20000000
def trapezoidal_rule(f, a, b, n):  # содержимое функции не менять
    """Вычисляет определенный интеграл функции f от a до b методом трапеций с n шагами."""
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    print(f'trapezoidal_rule = {integral * h}')


def sequence():
    # время старта start_time
    # вычисление fibonacci от значения 699998
    # вычисление trapezoidal_rule со значениями math.sin, 0, math.pi, 20000000
    # время окончания end_time
    print(f'sequence time: {end_time - start_time: 0.2f} \n')


def threads():
    # время старта start_time
    # вычисления на потоках:
    # 1. вычисление fibonacci от значения 699998
    # 2. вычисление trapezoidal_rule со значениями math.sin, 0, math.pi, 20000000
    # время окончания end_time
    print(f'threads time: {end_time - start_time: 0.2f} \n')


def processes():
    # время старта start_time
    # вычисления на процессах:
    # 1. вычисление fibonacci от значения 699998
    # 2. вычисление trapezoidal_rule со значениями math.sin, 0, math.pi, 20000000
    # время окончания end_time
    print(f'processes time: {end_time - start_time: 0.2f} \n')


if __name__ == '__main__':
    sequence()
    threads()
    processes()
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):
        
        fibonacci = 9
        trapezoidal_rule = 2.000000000000087
        sequence time:  ???
        
        fibonacci = 9
        trapezoidal_rule = 2.000000000000087
        threads time:  ??? 
        
        fibonacci = 9
        trapezoidal_rule = 2.000000000000087
        processes time:  ???
    """
