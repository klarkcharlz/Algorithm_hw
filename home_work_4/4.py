"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым
"""
from timeit import Timer

array = [1, 3, 1, 3, 4, 5, 1]*100


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(func_1())
print(func_2())

t1 = Timer("func_1()", globals=globals())
print("Version 1", t1.timeit(number=1_000), "seconds")
t2 = Timer("func_2()", globals=globals())
print("Version 2", t2.timeit(number=1_000), "seconds")

"""
Версия 2 показала гораздо более худший результат.

Первый вариант плох тем что мы проверяем количество вхождений в массив каждого эллемента,
даже  с учетом того что подобный элемент нам уже попадался и мы проводили для него аналогичную операцию,
что лишняя трата времени.

Во втором варианте проводится слишком много операций,
count, append, max, index что отнимает много времени в сумме.
"""


# написал и проверил свою версию
def func_3():
    max_num = array[0]
    max_count = array.count(max_num)
    for elem in set(array):
        cnt = array.count(elem)
        if cnt > max_count:
            max_count = cnt
            max_num = elem
    return f'Чаще всего встречается число {max_num}, ' \
           f'оно появилось в массиве {max_count} раз(а)'


print(func_3())
t3 = Timer("func_3()", globals=globals())
print("Version 3", t3.timeit(number=1_000), "seconds")

"""
Эта версия оказалась гораздо быстрее первых двух, впринципе она похожа на первую,
только мы не подсчитываем количество вхождений в массив тех эллементов которые нам уже попадались,
что сильно экономит время.
"""