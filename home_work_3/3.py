"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.
Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""


def unique(s):
    unique_list = []
    unique_set = set()
    k = 0
    for i in range(0, len(s)):
        for j in range(1 + k, len(s) + 1):
            if s[i:j] == s:
                continue
            hashing = hash(s[i:j])
            if hashing not in unique_list:
                unique_list.append(hashing)
            unique_set.add(s[i:j])
        k += 1
    return unique_list, unique_set


l, s = unique('papa')
print(len(l))  # -> 6
print(len(s))  # -> 6


