"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти)
И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
import timeit
import operator


# реализация взята с "https://webdevblog.ru/sortirovka-sliyaniem-merge-sort-v-python/"
def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


if __name__ == "__main__":
    # создадим 5 массивов вещественных чисел разной длины
    array_10 = [random.random() * random.randint(1, 50) for _ in range(10)]
    array_100 = [random.random() * random.randint(1, 50) for _ in range(100)]
    array_1000 = [random.random() * random.randint(1, 50) for _ in range(1000)]
    array_10000 = [random.random() * random.randint(1, 50) for _ in range(10000)]
    array_100000 = [random.random() * random.randint(1, 50) for _ in range(100000)]

    print("10:")
    print(timeit.timeit(
            "merge_sort(array_10[:])",
            globals=globals(),
            number=1_000))

    print("100:")
    print(timeit.timeit(
            "merge_sort(array_100[:])",
            globals=globals(),
            number=1_000))

    print("1000:")
    print(timeit.timeit(
            "merge_sort(array_1000[:])",
            globals=globals(),
            number=1_000))

    print("10000:")
    print(timeit.timeit(
            "merge_sort(array_10000[:])",
            globals=globals(),
            number=1_000))

    print("100000:")
    print(timeit.timeit(
            "merge_sort(array_100000[:])",
            globals=globals(),
            number=1_000))

"""
Замеры:
10: 0.009619106000172906
100: 0.14744349499960663
1000: 1.99389517399959
10000: 25.73112577200027
100000: 314.76428743500037
"""