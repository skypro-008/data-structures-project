class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node:param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        module_name = "__main__"
        class_name = self.__class__.__name__
        return f"<{module_name}.{class_name} object at {hex(id(self))}>"


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.data = []

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека
        :param data: данные, которые будут добавлены на вершину стека
        """

        self.data.append(data)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения
        :return: данные удаленного элемента
        """
        if len(self.data) > 0:
            delete = self.data.pop()
            return delete
        elif len(self.data) == 0:
            return None

    def top(self):
        return f"AttributeError: 'NoneType' object has no attribute 'data'"
