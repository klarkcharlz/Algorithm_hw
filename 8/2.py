"""
Задание 2.
Доработайте пример структуры "дерево",
рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)
Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""
# Добавил Валидацию


import sys


class TreeError(Exception):
    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return self.text


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = self.EmptyRoot()
        self.right_child = self.EmptyRoot()

    def insert_left(self, new_node):
        # добавил валидацию
        try:
            if new_node > self.root:
                raise TreeError(f"Левая Ветвь не может иметь значение выше корня(предыдущей Ветви).\nТекущее значение {self.root}," +
                                f" а вы пытаетесь вставить {new_node}.")
        except TreeError as err:
            print(err)
        else:
            if self.left_child is None:
                self.left_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj

    def insert_right(self, new_node):
        # добавил валидацию
        try:
            if new_node < self.root:
                raise TreeError(f"Правая Ветвь не может быть меньше корня(предыдущей Ветви).\nТекущее значение {self.root}," +
                                f"а вы пытаетесь вставить {new_node}.")
        except TreeError as err:
            print(err)
        else:
            if self.right_child is None:
                self.right_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        try:
            if obj > self.right_child or obj < self.left_child:
                raise TreeError(f"Неверное значение корня/Ветви.\nКорень\\Ветвь должны быть в диапазоне от {self.right_child}" +
                                f" до {self.left_child}.")
        except TreeError as err:
            print(err)
        else:
            self.root = obj

    def get_root_val(self):
        return self.root

    class EmptyRoot:
        @staticmethod
        def get_right_child(*args, **kwargs):
            return None

        @staticmethod
        def get_left_child(*args, **kwargs):
            return None

        @staticmethod
        def set_root_val(*args, **kwargs):
            return "Корень/Ветвь нельзя изменить, так как его не существует"

        @staticmethod
        def get_root_val(*args, **kwargs):
            return None

        def __str__(self):
            return "None"

        def __lt__(self, other):
            return other < (-sys.maxsize - 1)

        def __gt__(self, other):
            return other > sys.maxsize


if __name__ == "__main__":
    # проработаем на примере вашего кода, но с другими числами
    r = BinaryTree(12)
    print(r.get_root_val())  # 12
    print(r.get_left_child())  # None
    r.insert_left(50)  # Левая ветка не может иметь значение выше корня.
    print(r.get_left_child())  # None
    print(r.get_left_child().get_root_val())  # None
    r.insert_right(13)
    print(r.get_right_child())  # <__main__.BinaryTree object at 0x000001601B05B880>
    print(r.get_right_child().get_root_val())  # 13
    r.get_right_child().set_root_val(19)
    print(r.get_right_child().get_root_val())  # 19

    # проработаем простое древо, допустим как на этой картинке
    # https://myslide.ru/documents_3/55dc1299f892e1b49f1556a8bfa81822/img7.jpg
    print("-" * 100)  # sep
    tree = BinaryTree(8)  # корень
    print(tree.get_root_val())  # 8
    # левая ветка
    tree.insert_left(4)
    print(tree.get_left_child().get_root_val())  # 4
    tree.get_left_child().insert_left(2)
    tree.get_left_child().insert_right(6)
    print(tree.get_left_child().get_left_child().get_root_val())  # 2
    print(tree.get_left_child().get_right_child().get_root_val())  # 6
    tree.get_left_child().get_left_child().insert_left(1)
    tree.get_left_child().get_left_child().insert_right(3)
    tree.get_left_child().get_right_child().insert_left(5)
    tree.get_left_child().get_right_child().insert_right(7)
    print(tree.get_left_child().get_left_child().get_left_child().get_root_val())  # 1
    print(tree.get_left_child().get_left_child().get_right_child().get_root_val())  # 3
    print(tree.get_left_child().get_right_child().get_left_child().get_root_val())  # 5
    print(tree.get_left_child().get_right_child().get_right_child().get_root_val())  # 7
    # правая ветка
    tree.insert_right(12)
    tree.get_right_child().insert_right(14)
    tree.get_right_child().insert_left(10)
    tree.get_right_child().get_right_child().insert_right(15)
    tree.get_right_child().get_right_child().insert_left(13)
    tree.get_right_child().get_left_child().insert_left(9)
    tree.get_right_child().get_left_child().insert_right(11)

    # попробую нарисовать дерево
    print(f"""
     ____{tree.get_root_val()}____
    /         \\
   {tree.get_left_child().get_root_val()}          {tree.get_right_child().get_root_val()}
  / \\        /  \\
 {tree.get_left_child().get_left_child().get_root_val()}   {tree.get_left_child().get_right_child().get_root_val()}      {tree.get_right_child().get_left_child().get_root_val()}  {tree.get_right_child().get_right_child().get_root_val()}
/ \\ / \\    / \\ /  \\
{tree.get_left_child().get_left_child().get_left_child().get_root_val()} {tree.get_left_child().get_left_child().get_right_child().get_root_val()} {tree.get_left_child().get_right_child().get_left_child().get_root_val()} {tree.get_left_child().get_right_child().get_right_child().get_root_val()}   {tree.get_right_child().get_left_child().get_left_child().get_root_val()} {tree.get_right_child().get_left_child().get_right_child().get_root_val()} {tree.get_right_child().get_right_child().get_left_child().get_root_val()} {tree.get_right_child().get_right_child().get_right_child().get_root_val()}
    """)


"""
Выглядит страшно и не по PEP-8, но вот что получилось:
     ____8____
    /         \
   4          12
  / \        /  \
 2   6      10  14
/ \ / \    / \ /  \
1 3 5 7   9 11 13 15
"""
