class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None
        self.queue_data = []

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if len(self.queue_data) == 0:
            new_node = Node(data, None)
            self.queue_data.insert(0, new_node)
        else:
            new_node = Node(data, None)
            self.queue_data[0].next_node = new_node
            self.queue_data.insert(0, new_node)

        if self.tail is not None:
            self.head = self.queue_data[len(self.queue_data) - 1]
            self.tail = self.queue_data[0]
        else:
            self.head = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        result = []
        for node in self.queue_data:
            result.append(node.data)
        result.reverse()
        return "\n".join(result)



