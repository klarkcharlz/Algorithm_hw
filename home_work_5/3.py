"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям
И добавить аналитику, так ли это или нет.!
"""
from collections import deque
from timeit import Timer


# создадим одинаковые list и deque
my_list = [num ** 2 for num in range(1, 100_000)]
my_deque = deque(my_list)

# оценим скорость выполнения одинаковых операций
# append
t1 = Timer("""
for i in range(100_000):
    my_list.append(i ** 2)
""",
           globals=globals())
t2 = Timer("""
for i in range(100_000):
    my_deque.append(i ** 2)
""",
           globals=globals())

print("List append method ", t1.timeit(number=1_000), "seconds")
print("Deque append method ", t2.timeit(number=1_000), "seconds")

# pop
t1 = Timer("""
for _ in range(100_000):
    my_list.pop()
""",
           globals=globals())
t2 = Timer("""
for _ in range(100_000):
    my_deque.pop()
""",
           globals=globals())

print("List pop method ", t1.timeit(number=1_000), "seconds")
print("Deque pop method ", t2.timeit(number=1_000), "seconds")

"""
Мои результаты:
List append method  19.783154923999973 seconds
Deque append method  19.296151148999343 seconds
List pop method  4.3814361529985035 seconds
Deque pop method  4.096262449998903 seconds
Время выполнения аналогичных методов что для list что для Deque практически одинаковое.
Хотя Deque всеравно немного выйгрывает при каждом запуске.
Теперь сравним преимущество специализированных методов Deque, перед аналогичными в list.
"""

# deque.appendleft(x) vs list.insert(0, x)
t1 = Timer("""
for i in range(100_000):
    my_list.insert(0, i ** 2)
""",
           globals=globals())
t2 = Timer("""
for i in range(100_000):
    my_deque.appendleft(i ** 2)
""",
           globals=globals())

print("List insert 0 method ", t1.timeit(number=10), "seconds")
print("Deque appendleft method ", t2.timeit(number=10), "seconds")


# deque.popleft() vs list.pop(0)
t1 = Timer("""
for _ in range(100_000):
    my_list.pop(0)
""",
           globals=globals())
t2 = Timer("""
for i in range(100_000):
    my_deque.popleft()
""",
           globals=globals())

print("List pop 0 method ", t1.timeit(number=10), "seconds")
print("Deque popleft method ", t2.timeit(number=10), "seconds")
"""
мои результаты:
List insert 0 method  211.20098975699875 seconds
Deque appendleft method  0.19299068899999838 seconds
List pop 0 method  80.80609748999996 seconds
Deque popleft method  0.077603640002053 seconds
Результаты поражают, Deque вне конкуренции.
"""

