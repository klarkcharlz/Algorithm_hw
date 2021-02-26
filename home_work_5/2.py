"""
2.*	Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
__mul__
__add__
Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
1. вариант
defaultdict(list)
int(, 16)
reduce
2. вариант
class HexNumber:
    __add__
    __mul__
hx = HexNumber
hx + hx
"""
from collections import namedtuple
from re import fullmatch


def hex_num():
    """Валидация ввода"""
    while True:
        num = input("Пожалуйста введи шестнадцатиричное число вида A2 и C4F:\n")
        if fullmatch(r"[0-9A-F]+", num):
            break
    return num


# введем показания как в примере A2 и C4F
number_1 = hex_num()  # A2
number_2 = hex_num()  # C4F


# Вариант 2 через ООП
class HexNumber:
    def __init__(self, hx: str):
        self.hx = list(hx)

    def __add__(self, other):
        """так много операций что бы ответ соответсвовал условию, вывод в виде массива"""
        return list(str(hex(int("".join(self.hx), 16) + int("".join(other.hx), 16)))[2:].upper())

    def __mul__(self, other):
        return list(str(hex(int("".join(self.hx), 16) * int("".join(other.hx), 16)))[2:].upper())


print("ООП")
nex_number_1 = HexNumber(number_1)
nex_number_2 = HexNumber(number_2)
print(nex_number_1.hx)  # -> [‘A’, ‘2’]
print(nex_number_2.hx)  # -> [‘C’, ‘4’, ‘F’]
print(nex_number_1 + nex_number_2)  # -> [‘C’, ‘F’, ‘1’]
print(nex_number_1 * nex_number_2)  # -> [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]


# Вариант 1 через collections - namedtuple
hex_tuple = namedtuple("HexNumber", "hex_mass")
nex_number_1 = hex_tuple(hex_mass=list(number_1))
nex_number_2 = hex_tuple(hex_mass=list(number_2))

print("collections - namedtuple")
print(nex_number_1.hex_mass)  # -> [‘A’, ‘2’]
print(nex_number_2.hex_mass)  # -> [‘C’, ‘4’, ‘F’]


def add_mul_name_tuple_hex(operation, obj1, obj2):
    """функция для выполнения математический операций на namedtuple"""
    if operation == "*":
        return list(str(hex(int("".join(obj1), 16) * int("".join(obj2), 16)))[2:].upper())
    if operation == "+":
        return list(str(hex(int("".join(obj1), 16) + int("".join(obj2), 16)))[2:].upper())


print(add_mul_name_tuple_hex("+", nex_number_1.hex_mass, nex_number_2.hex_mass))  # -> [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]
print(add_mul_name_tuple_hex("*", nex_number_1.hex_mass, nex_number_2.hex_mass))  # -> [‘C’, ‘F’, ‘1’]

"""
Проверял на множестве комбинацай, всё совпало. Проверял по калькулятору.
"""