"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""
# к моему разочарованию, для меня тема оказалась очень сложной, изменил вашу версию, сделал на основе классов


from collections import Counter, deque


class HaffmanCode:
    """Класс для реализации получения кода Хаффмана"""
    def __init__(self, string: str):
        self.string = string  # сохраняю строку для метода __str__
        self.haff_tree = self.HaffmanTree(self.string).sorted_tree  # получаю дерево
        self.code_table = self.__haffman_code()  # получаем код

    def __haffman_code(self):
        """Метод служит для получения кода строки 'по Хаффману'"""
        tree = self.haff_tree
        code = {}

        def get_code(tree, path=''):
            if not isinstance(tree, dict):
                code[tree] = path
            else:
                get_code(tree[0], path=f'{path}0')
                get_code(tree[1], path=f'{path}1')
        get_code(tree)
        return code

    def __str__(self):
        """для вывода кода при использовании функции print(HaffmanCode)"""
        code = ""
        for char in self.string:
            code += f"{self.code_table[char]} "
        return code

    class HaffmanTree:
        """Класс для получения сортированного древа для кодировки строки по Хаффману"""
        def __init__(self, string: str):
            self.sorted_tree = self.__sorted_elements(string)

        def __sorted_elements(self, string: str):
            """Ваша функция, взята с кодов к урокам"""
            sorted_elements = deque(sorted(Counter(string).items(), key=lambda item: item[1]))
            if len(sorted_elements) != 1:
                while len(sorted_elements) > 1:
                    weight = sorted_elements[0][1] + sorted_elements[1][1]
                    comb = {0: sorted_elements.popleft()[0],
                            1: sorted_elements.popleft()[0]}
                    for i, _count in enumerate(sorted_elements):
                        if weight > _count[1]:
                            continue
                        else:
                            sorted_elements.insert(i, (comb, weight))
                            break
                    else:
                        sorted_elements.append((comb, weight))
            else:
                weight = sorted_elements[0][1]
                comb = {0: sorted_elements.popleft()[0], 1: None}
                sorted_elements.append((comb, weight))
            return sorted_elements[0][0]


if __name__ == "__main__":
    s = "beep boop beer!"
    haffman_code = HaffmanCode(s)
    # проверка
    print(haffman_code.string)  # -> beep boop beer!
    print(haffman_code.haff_tree)  # -> {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
    print(haffman_code.code_table)  # -> {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
    print(haffman_code)  # -> "00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001"
    """
    Всё совпадает с вашими результатами.
    """



