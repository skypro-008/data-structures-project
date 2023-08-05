from src.node import Node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        self.top = Node(data, self.top)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        data = self.top.data
        self.top = self.top.next_node
        return data

    def count(self):
        """функция счета количества элементов стека"""

        count = 0
        try:
            node = self.top.next_node
            while True:
                count += 1
                node = node.next_node
        except AttributeError:
            return count

    def __str__(self):
        return f'Stack. Количество элементов - {self.count()}'
