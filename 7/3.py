"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.
Задачу можно решить без сортировки исходного
массива.
Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...
[5, 3, 4, 3, 3, 3, 3]
[3, 3, 3, 3, 3, 4, 5]
my_lst
new_lts
arr[m]
from statistics import median
[3, 4, 3, 3, 5, 3, 3]
left.clear()
right.clear()
m = 3
len = 7
i
left = []
right = []
left == right and
for i in
    for
    left == right
    left.clear()
    right.clear()
"""
import random
from statistics import median


def input_m():
    while True:
        try:
            m = int(input("Пожалуйста введите число, а я на его основе построю случайный массив чисел по формуле:"
                          "'2m + 1':\n"))
            if m <= 0:
                raise ValueError
        except ValueError:
            print("Пожалуйста вводите целое положительное число.")
        else:
            break
    return m


# реализация взята с "https://habr.com/ru/post/414653/"
def gnome(data):
    """Гномья сортировка."""
    i, j, size = 1, 2, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i, j = j, j + 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return data


if __name__ == "__main__":
    m = input_m()
    orig_list = [random.randint(-1_000_000, 1_000_000) for _ in range((2 * m) + 1)]
    print(f"Медианное значение Вашего массива равно: {gnome(orig_list[:])[m]}.")
    # проверка
    print(gnome(orig_list[:])[m] == median(orig_list[:]))  # -> True
