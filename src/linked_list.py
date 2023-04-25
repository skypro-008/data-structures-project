class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    def __str__(self):
        return self.data


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        self.head = None
        self.tail = None


    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

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
        return ll_string[1: len(ll_string)]

    def remove_first(self):
        """Удаление данных с начала списка"""
        if not self.head:
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next_node
        return data

    def remove_last(self):
        """удаление данных с конца списка"""
        if not self.head:
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next_node != self.tail:
                current = current.next_node
            current.next_node = None
            self.tail = current
        return data

    def to_list(self):
        """Вывод данных односвязного списка в виде списка"""
        node = self.head

        self.new_list = []
        while node:
            self.new_list.append(node.data)
            node = node.next_node

        return self.new_list

    def get_data_by_id(self, element):
        """"""
        LinkedList.to_list(self)

        for i in self.new_list:
            if i['id'] == element:
                return i







