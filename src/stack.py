class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node





class Stack:
    """Класс для стека"""

    def __init__(self):
        self.top = None

    def __str__(self):
        return str(self.top)

    def push(self, data):
        new_node = Node(data, self.top)
        self.top = new_node

    def pop(self):
        data = self.top.data
        self.top = self.top.next_node
        return data


