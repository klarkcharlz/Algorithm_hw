"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import Timer


nums = [num for num in range(1, 100_000)]


# Оригинальный вариант
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


t1 = Timer("func_1(nums)", globals=globals())
print("Original", t1.timeit(number=1_000), "seconds")
"""В моем случае при каждом запуске было около 5.5 секунд"""


# Вараинт после оптимизации
def func_2(nums):
    return [i for i in range(1, len(nums)) if nums[i] % 2 == 0]


t1 = Timer("func_2(nums)", globals=globals())
print("Optimizations ", t1.timeit(number=1_000), "seconds")
"""Так как все встроенные возможности Python заточены под скорость применил
генератор списка, и выйграл 1 секунду.
"""
