"""
Задание 2.
Реализуйте два алгоритма.
Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.
Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.
Не забудьте указать где какая сложность.
Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""
from random import randint
from time import time


random_list = [randint(1, 1001) for _ in range(100_000)]


# O(n^2)
def hard_min(l):
    min_num = l[0]
    for i in l:
        for j in l:
            if i < j:
                min_n = i
            else:
                min_n = j
        if min_n < min_num:
            min_num = min_n
    return min_num


# O(n)
def linear_min(l):
    min_num = l[0]
    for num in l[1:]:
        if num < min_num:
            min_num = num
    return min_num


start = time()
min_num = hard_min(random_list)
print(time() - start)
print(min_num == min(random_list))  # проверка

start = time()
min_num = linear_min(random_list)
print(time() - start)
print(min_num == min(random_list))  # проверка

