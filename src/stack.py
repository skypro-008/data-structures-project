class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None
        self.size = 0

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        self.top = Node(data, self.top)
        self.size += 1

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.size == 0:
            return 'No elements in stack'
        result = self.top.data
        self.top = self.top.next_node
        self.size -= 1
        return result

    def __str__(self):
        top = self.top if self.top is None else self.top.data
        return f'Class_name: {self.__class__.__name__}, Top of stack: {top}, Size of stack: {self.size}'






