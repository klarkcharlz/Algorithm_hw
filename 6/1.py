"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.
Можно взять задачи с курса Основ
или с текущего курса Алгоритмов
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

import memory_profiler
from timeit import default_timer
from pympler import asizeof


# Воспользуюсь Вашим декоратором немного изменив его
def profile(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        start = default_timer()
        func(*args, **kwargs)
        print(f"Время выполнения функции {func.__name__} : {default_timer() - start}.")
        m2 = memory_profiler.memory_usage()
        memory_diff = m2[0] - m1[0]
        return memory_diff
    return wrapper


# Первый скрипт,
# взял свой код с предыдущего урока,
# в данном случае применим ООП слоты в качестве оптимизаци и посмотрим
class HexNumber:
    def __init__(self, hx: str):
        self.hx = list(hx)

    def __add__(self, other):
        """так много операций что бы ответ соответсвовал условию, вывод в виде массива"""
        return HexNumber(list(str(hex(int("".join(self.hx), 16) + int("".join(other.hx), 16)))[2:].upper()))

    def __mul__(self, other):
        return HexNumber(list(str(hex(int("".join(self.hx), 16) * int("".join(other.hx), 16)))[2:].upper()))

    def __str__(self):
        return self.hx


class HexNumberWithSlots:
    __slots__ = ['hx', ]

    def __init__(self, hx: str):
        self.hx = list(hx)

    def __add__(self, other):
        """так много операций что бы ответ соответсвовал условию, вывод в виде массива"""
        return HexNumberWithSlots(list(str(hex(int("".join(self.hx), 16) + int("".join(other.hx), 16)))[2:].upper()))

    def __mul__(self, other):
        return HexNumberWithSlots(list(str(hex(int("".join(self.hx), 16) * int("".join(other.hx), 16)))[2:].upper()))

    def __str__(self):
        return self.hx


hex_1 = HexNumber("C4")
hex_2 = HexNumberWithSlots("A3F")

print("TEST 1\nSLOTS")
print(f"obj without slots size of : {asizeof.asizeof(hex_1)}")
print(f"obj with slots size of : {asizeof.asizeof(hex_2)}")

"""
obj without slots size of : 392
obj with slots size of : 288
Как видим обьекты со слотами занимают меньше места
"""


# Повыполняем абстрактные вычисления для измерения памяти

@profile
def no_slots_test():
    """Операци с обьектом без слотов"""
    hex_list = []
    for i in range(10_000_000):
        hex_list.append(hex_1 + hex_1)
    for i in range(10_000_000):
        hex_list.append(hex_1 * hex_1)
    return hex_list


@profile
def slots_test():
    """Операции с обьектом со слотами"""
    hex_list = []
    for i in range(10_000_000):
        hex_list.append(hex_2 + hex_2)
    for i in range(10_000_000):
        hex_list.append(hex_2 * hex_2)
    return hex_list


print(f"Выполнение без слотов занимает : {no_slots_test()}.")
print(f"Выполнение со слотами занимает : {slots_test()}.")

"""
TEST 1
SLOTS
Время выполнения функции no_slots_test : 38.925580811000145.
Выполнение без слотов занимает : 3.5546875.
Время выполнения функции slots_test : 27.38269593799987.
Выполнение со слотами занимает : 1.12890625.t
Как видим вариант со слотами занимает в 2 раза меньше оперативной памяти.
"""


# Скрипт 2, проверим оптимизацию с помощью функции map
# допустим стоит цель создать список квадратов


@profile
def square():
    square_list = []
    for num in range(1, 100_000_000):
        square_list.append(num * num)
    return square_list


@profile
def square_map():
    square_map = map(lambda num: num * num, range(1, 100_000_000))
    return list(square_map)


print("TEST 2\nMAP")
print(f"Выполнение без map занимает : {square()}.")
print(f"Выполнение с map занимает : {square_map()}.")

"""
TEST 2
MAP
Время выполнения функции square : 18.4209034.
Выполнение без map занимает : 0.53125.
Время выполнения функции square_map : 17.4563671.
Выполнение с map занимает : 0.08203125.
Как видим вариант с map реально экономит память.
"""


# Скрипт 3, ленивые вычисления
@profile
def with_list():
    my_list = [num for num in range(1, 300_000_000)]
    for elem in my_list:
        n = elem


@profile
def with_gen():
    my_gen = (num for num in range(1, 5_000_000_000))
    for elem in my_gen:
        n = elem


print("TEST 3\nGENERATOR")
print(f"Выполнение с списком занимает : {with_list()}.")
print(f"Выполнение с генератором занимает : {with_gen()}.")

"""
TEST 3
GENERATOR
Время выполнения функции with_list : 10.892661901999872.
Выполнение с списком занимает : 3.43359375.
Время выполнения функции with_gen : 171.59065841499978.
Выполнение с генератором занимает : 0.0.
Как видим применение генераторов тоже экономит память.
Как я не увеличивал range для варианта с генератором, результаты по нулям, 
но я думаю уже наглядно видно насколько этот вариант лучше.
Генератор не хранится в памяти целиком, а лишь возвращает по одному значению по запросу.
"""
