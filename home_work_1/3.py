"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
from random import randint


company = {
    "company_1": randint(100_000, 1_000_000),
    "company_2": randint(100_000, 1_000_000),
    "company_3": randint(100_000, 1_000_000),
    "company_4": randint(100_000, 1_000_000),
    "company_5": randint(100_000, 1_000_000),
    "company_6": randint(100_000, 1_000_000),
    "company_7": randint(100_000, 1_000_000),
    "company_8": randint(100_000, 1_000_000),
    "company_9": randint(100_000, 1_000_000),
    "company_10": randint(100_000, 1_000_000),
}


"""
Вариант 1. n*len(...) + n^2*logn
Очень медленный по скорости выполнения вариант.
Сужу по графику из материалов к уроку.
"""
company_items = list(company.items())  # O(1) * O(len(...)) * O(n) = n*len(...)
company_items.sort(key=lambda i: i[1], reverse=True)  # O(n*logn) * O(n) = n^2*logn
print("Топ 3 компаний с самой большой прибылью:")
[print(f"{comp[0]}: {comp[1]}") for comp in company_items[:3]]

"""
Вариант 2. n^3*logn + 2 + n^5
Ужасно медленный вариант, гораздо хуже первого.
"""
sorted_values = sorted(company.values(), reverse=True)[:3]  # O(1) * O(n*logn) * O(n) * O(n) = n^3*logn
sorted_dict = {}  # O(1)
for i in sorted_values:  # 0(n)
    for k in company:  # O(n)
        if company[k] == i:  # O(n) * O(1) = n
            sorted_dict[k] = company[k]  # O(n) * O(1) * O(n) = n^2
            break  # O(1)
print("Топ 3 компаний с самой большой прибылью:")
print(sorted_dict)
