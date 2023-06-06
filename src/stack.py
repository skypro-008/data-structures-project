class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        :param next_node: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        """Возвращает строковое представление стека"""
        return self._str_recursive(self.top)

    def _str_recursive(self, current_node):
        """Рекурсивная функция для формирования строки из узлов стека"""
        if current_node is None:
            return ""
        else:
            return f"{current_node.data} -> {self._str_recursive(current_node.next_node)}"

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next_node = self.top
            self.top = new_node

    def pop(self):
        """Метод возвращает элемент с вершины, удаляя его из стека"""
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next_node

        return data



