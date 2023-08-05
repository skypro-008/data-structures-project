from src.node import Node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        element = Node(data)
        if self.tail is None:
            self.tail = element
            self.head = element
        else:
            self.tail.next_node = element
            self.tail = element

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        element = self.head.data
        self.head = self.head.next_node
        return element

    def __str__(self):
        """Магический метод для строкового представления объекта"""

        list_ = list()
        node = self.head
        while node is not None:
            list_.append(str(node.data))
            node = node.next_node
        return '\n'.join(list_)
