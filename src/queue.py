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
        self.queue = str()
        self.tail = None

    def __repr__(self):
        """
        Магический метод для отображения информации об объекте класса в режиме отладки
        """
        return self.queue[:-1]

    def __str__(self):
        """
        Магический метод для строкового представления объекта пользователю
        """
        return self.queue[:-1]

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data, None)
        node.next_node = None
        if self.head == None:
            self.head = node    # если список пуст, то новый узел идет первым
            self.tail = self.head    # находим последний узел в списке
            self.queue += f"{self.head.data}\n"
        else:
            self.tail.next_node = node    # добавляем новый узел
            self.tail.next_node.next_node = self.head
            self.tail = self.tail.next_node
            self.tail.next_node = None
            self.queue += f"{self.tail.data}\n"

    def dequeue(self, data):
        """
        Метод для удаления элемента из очереди и его возвращения

        :return: данные удаленного элемента
        """
        pass