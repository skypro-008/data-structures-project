class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        self.head = Node(data, self.head)
        if self.tail is None:
            self.tail = self.head

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_tail = Node(data, None)
        if self.tail is not None:
            self.tail.next_node = new_tail
        else:
            self.head = new_tail
        self.tail = new_tail

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.lstrip()
