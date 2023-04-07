class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data=None, next_node=None):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = Node

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        lastnode = self.head
        while (lastnode.next_node):
            lastnode = lastnode.next_node
        lastnode.next_node = node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self) -> list:
        """Возвращает список с данными"""
        node = self.head

        ll_string = []
        while node:
            ll_string.append(str(node.data))
            node = node.next_node

        return ll_string

    def get_data_by_id(self, key):
        node = self.head

        while node:
            try:
                if node.data.get('id') == key:
                    result = node.data
                node = node.next_node
            except AttributeError:
                print("Не является словарем или нет id")
                node = node.next_node
        return result
