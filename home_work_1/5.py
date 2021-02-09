"""
Задание 5.
Задание на закрепление навыков работы со стеком
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.
После реализации структуры, проверьте ее работу на различных сценариях
Подсказка:
Отдельне стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""


class Stack:
    """LIFO. Последним пришол первым ушел."""
    def __init__(self, max_plates):
        self.max_plates = max_plates  # максимальное количество чашек в стопке
        self.stacks = []  # собранные стопки
        self.stack = []  # текущая стопка

    class StackOfPlates:
        """Наполненная чашками стопка"""
        def __init__(self, n):
            self.stack = ["plates"] * n

    def add(self, n):
        """Добавление чашек"""
        for _ in range(n):
            self.stack.append("plate")
            # если стопка собрана, оставляем ее в сторону и начинаем собирать новую
            if len(self.stack) == self.max_plates:
                self.stacks.append(self.StackOfPlates(self.max_plates))
                self.stack = []

    def sub(self, n):
        """Убираем чашки"""
        for _ in range(n):
            if self.stack:
                self.stack.pop()
                if len(self.stack) == 0:
                    if self.stacks:
                        self.stack = self.stacks.pop().stack
                    else:
                        print("Чашки закончились.")
                        break
            else:
                print("Чашки закончились.")
                break

    def __str__(self):
        plates_info = ""
        if self.stacks:
            plates_info += f"Собрано {len(self.stacks)} стопок по {self.max_plates} чашек."
        if self.stack:
            plates_info += f"В набираемой стопке {len(self.stack)} чашек."
        plates_info += f"Всего: {len(self.stacks) * self.max_plates + len(self.stack)} чашек."
        return plates_info


stacks = Stack(10)  # создаем стек, максимальное количество чашек в стопке 10
# поманипулируем со стеком
stacks.add(22)
print(stacks)
stacks.sub(7)
print(stacks)
stacks.sub(8)
print(stacks)
stacks.sub(1000)
print(stacks)
