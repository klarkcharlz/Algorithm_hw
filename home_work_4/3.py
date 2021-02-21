"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Сделайте вывод, какая из трех реализаций эффективнее и почему!!!
И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""
from timeit import Timer
from random import randint
from cProfile import run


nums = randint(100_000, 1_000_000)


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


t1 = Timer("revers_1(nums)", globals=globals())
print("Version 1 ", t1.timeit(number=10_000_000), "seconds.", f"Result: {revers_1(nums)}.")
t2 = Timer("revers_2(nums)", globals=globals())
print("Version 2 ", t2.timeit(number=10_000_000), "seconds", f"Result: {revers_2(nums)}.")
t3 = Timer("revers_3(nums)", globals=globals())
print("Version 3 ", t3.timeit(number=10_000_000), "seconds", f"Result: {revers_3(nums)}.")

"""
1 вараинт самый медленнный. Так как это рекурсия, она образует стек.
3 вариант самый быстрый. Пользуемся встроенными инструментами Python заточенными на скорость уже до нас.
"""

# Анализ через cProfile


def main():
    revers_1(nums)
    revers_2(nums)
    revers_3(nums)


run('main()')
