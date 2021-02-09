"""
Задание 6.
Задание на закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После реализации структуры, проверьте ее работу на различных сценариях
"""


class Turn:  # класс очередь
    """FIFO. Первым пришел, первым ушел."""

    class Revision:
        """Очередь на доработку"""
        def __init__(self):
            self.rev_tasks = []

        def add_task(self, task):
            """Добавить задачу на доработку"""
            self.rev_tasks.insert(0, task)

        def sub_task(self, other):
            """Выполнить задачу и отправить в решенные"""
            other.completed_task.append(self.rev_tasks.pop())

        # реализовал их для возможности итерирования по задачам
        def __iter__(self):
            self.i = -1
            return self

        def __next__(self):
            self.i += 1
            if self.i == len(self.rev_tasks):
                raise StopIteration
            else:
                return self.rev_tasks[self.i]

    def __init__(self):
        """Создается очередь задач"""
        self.new_tasks = []  # список не решенных задач
        self.completed_task = []  # список решенных задач
        self.revision_tasks = self.Revision()  # очередь на доработку

    class Task:
        """Новая задача"""
        def __init__(self, text):
            self.text = text  # текст задачи

        def __str__(self):
            return f"Что нужно сделать: {self.text}."

    def add_task(self, text):
        """Создание задачи и добавление ее в очередь"""
        new_task = self.Task(text)
        self.new_tasks.insert(0, new_task)

    def completed(self):
        """Выполнение задачи"""
        self.completed_task.append(self.new_tasks.pop())

    def revision(self):
        """Отправка задачи в очередь на доработку"""
        self.revision_tasks.add_task(self.new_tasks.pop())

    def finalize(self):
        """Доработка задачи из очереди на доработку и отправка ее в решенные задачи"""
        self.revision_tasks.sub_task(self)


turn = Turn()  # Создаем очередь
# насоздаем задач
turn.add_task("Выучить Python")
turn.add_task("Сделать домашнее задание")
turn.add_task("Сделать чтонибудь полезное")
# посмотрим что нужно сделать
print("Очередь задач:")
for task in turn.new_tasks:
    print(task)
print("Выполним одну задачу в очереди.")
turn.completed()  # выполним задачу согласно очереди
# проверим что выполнилась задача которая первой попала в очередь
print("Оставшиеся задачи: ")
for task in turn.new_tasks:
    print(task)
# отправим оставшиеся задачи на доработку
print("Отправляем задачи на доработку")
turn.revision()
turn.revision()
# посмотрим список задач на доработке
print("задачи на доработку: ")
for task in turn.revision_tasks:
    print(task)
# доработаем их и отправим в решенные
print("Доработаем задачи находящиеся на доработке.")
turn.finalize()
turn.finalize()
print("Посмотрим все что мы выполнили в порядке выполнения")
for task in turn.completed_task:
    print(task)
