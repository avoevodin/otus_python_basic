"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return list(num ** 2 for num in nums)


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    """
    returns true if the num is prime, else returns false.
    """
    is_prime_number = num > 1
    if is_prime_number:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                is_prime_number = False
                break
    return is_prime_number


def filter_numbers(numbers, nums_filter):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if nums_filter == ODD:
        func = (lambda x: x % 2 == 1)
    elif nums_filter == EVEN:
        func = (lambda x: x % 2 == 0)
    else:
        func = is_prime

    return list(filter(func, numbers))
