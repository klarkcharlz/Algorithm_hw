"""
Задание 5.**
Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).
Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)
Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснвование рез-ам
"""
from timeit import Timer


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


print(simple(10))  # -> 29
print(simple(100))  # -> 41
print(simple(1000))  # -> 7919


t1 = Timer("simple(10)", globals=globals())
print("simple 10 ", t1.timeit(number=100), "seconds")
t2 = Timer("simple(100)", globals=globals())
print("simple 100 ", t2.timeit(number=100), "seconds")
t3 = Timer("simple(1000)", globals=globals())
print("simple 1000 ", t3.timeit(number=100), "seconds")


"""
Вариант через решето написанный мною.
Согласно алгоритму по ссылке https://younglinux.info/algorithm/sieve.
Написал следующую реализацию.
"""


def sieve_of_eratosthenes(i):
    simple_numbers = [2, 3]
    count = 2
    num = 4
    while count != i:
        for elem in simple_numbers:
            if num % elem == 0:
                break
        else:
            simple_numbers.append(num)
            count += 1
        num += 1
    return simple_numbers[i - 1]


print(sieve_of_eratosthenes(10))  # -> 29
print(sieve_of_eratosthenes(100))  # -> 541
print(sieve_of_eratosthenes(1000))  # -> 7919
# результаты верны

t4 = Timer("sieve_of_eratosthenes(10)", globals=globals())
print("sieve_of_eratosthenes 10 ", t4.timeit(number=100), "seconds")
t5 = Timer("sieve_of_eratosthenes(100)", globals=globals())
print("sieve_of_eratosthenes 100 ", t5.timeit(number=100), "seconds")
t6 = Timer("sieve_of_eratosthenes(1000)", globals=globals())
print("sieve_of_eratosthenes 1000 ", t6.timeit(number=100), "seconds")

"""
Результаты поражают.
Улучшение по скорости для 1000-го эллемента в моём случае было 23,5 секунды.
Уменьшилось с 25 секунд до 1,5.
"""

