class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node = None):
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
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека
        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node
        self.data.append(data)
        return self.data

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения
        :return: данные удаленного элемента
        """
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = popped_node.next_node
            self.data.pop()
            return popped_node.data
