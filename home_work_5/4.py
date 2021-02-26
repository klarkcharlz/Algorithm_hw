"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import Timer


# создадим обычный dict и OrderedDict для сравнения
my_dict = {i: i ** 2 for i in range(1, 100_000)}
my_order_dict = OrderedDict(my_dict.items())

# выполним ряд аналогичных действий над обоими обьектами
print("Взятие по ключу:")
t1 = Timer("""
for key in my_dict:
    val = my_dict[key]
""", globals=globals())
print("Dict test_1, my_dict[key]", t1.timeit(number=1_000), "seconds")
t2 = Timer("""
for key in my_order_dict:
    val = my_order_dict[key]
""", globals=globals())
print("OrderedDict test_1, my_order_dict[key]", t2.timeit(number=1_000), "seconds")

print("Удаление последней пары ключ-значение:")
t1 = Timer("""
val = my_dict.popitem()
""", globals=globals())
print("Dict test_2, popitem()", t1.timeit(number=1_000), "seconds")
t2 = Timer("""
val = my_order_dict.popitem()
""", globals=globals())
print("OrderedDict test_2, popitem()", t2.timeit(number=1_000), "seconds")

print("Обновление:")
t1 = Timer("""
for i in range(100_000):
    my_dict.update([(i, i ** 2)])
""", globals=globals())
print("Dict test_3, update()", t1.timeit(number=1_000), "seconds")
t2 = Timer("""
for i in range(100_000):
    my_order_dict.update([(i, i ** 2)])
""", globals=globals())
print("OrderedDict test_3, update()", t2.timeit(number=1_000), "seconds")

"""
Мои значения:
Dict test_1, my_dict[key] 2.9754148819993134 seconds
OrderedDict test_1, my_order_dict[key] 3.4475242890002846 seconds
Удаление случайной пары ключ-значение:
Dict test_2, popitem() 5.6259999837493524e-05 seconds
OrderedDict test_2, popitem() 0.00013002999912714586 seconds
Обновление:
Dict test_3, update() 30.766754578002292 seconds
OrderedDict test_3, update() 36.48830636900311 seconds
Как видим все операции кроме popitem() в обычном dict выполняются быстрее,
но для popitem() в OrderedDict() скорость выполнения ГОРАЗДО быстрее.
Почему сказать затрудняюсь, ведь согласно документации с версии Python 3.6 
обычный словарь сохраняет порядок вставки элементов, и метод popitem() удаляет последнюю пару
ключ-значения, так же как и в OrderedDict.
Я думаю что имеет смысл использовать OrderedDict только в том случае, если мы собираемся запускать наш код
и на более старых версиях Python чем 3.6.
Иначе в этом нету смысла, сохранение порядка вставки нам гарантирует и обычный Dict.
"""
