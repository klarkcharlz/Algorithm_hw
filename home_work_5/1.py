"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1
Предприятия, с прибылью ниже среднего значения: Фирма_2
"""
from collections import namedtuple
import re


"""
Для своего варианта реализации я выбрал namedtuple.
"""


def count_company():
    """Добиваемся от пользователя ввода положительного целого числа"""
    while True:
        try:
            n = int(input("Информацию о скольки компаниях Вы хотите внести?\n"))
            if n <= 0:
                raise ValueError
        except ValueError:
            print("Пожалуйста вводите целое положительное число!")
        else:
            break
    return n


def create_obj():
    """создаем экземпляры namedtuple"""
    comp_name = input("Пожалуйста введите имя компании:\n")
    while True:
        profit = input("Пожалуйста ввведите прибыль компании за каждый месяц через пробел:\n")
        if re.fullmatch(r'\d+(.\d+)?\s\d+(.\d+)?\s\d+(.\d+)?\s\d+(.\d+)?', profit):
            break
    res = namedtuple('income_information', 'company_name annual_profit')
    return res(company_name=comp_name, annual_profit=sum(list(map(float, profit.split()))))


def avg_profit():
    cnt = 0
    sum_prof = 0
    for comp in company_list:
        cnt += 1
        sum_prof += comp.annual_profit
    return sum_prof / cnt


if __name__ == '__main__':
    n = count_company()  # количество компаний для заполнения
    company_list = []  # список наших будущих компаний
    while n > 0:  # заполняем список
        company_list.append(create_obj())
        n -= 1
    # ищем среднюю годовую прибыль всех предприятий
    avg_prof = avg_profit()
    # Выводим информацию
    print(f"Средняя годовая прибыль всех предприятий: {avg_prof}.")
    print("Предприятия, с прибылью выше среднего значения:")
    [print(comp.company_name) for comp in company_list if comp.annual_profit > avg_prof]
    print("Предприятия, с прибылью ниже среднего значения:")
    [print(comp.company_name) for comp in company_list if comp.annual_profit < avg_prof]
