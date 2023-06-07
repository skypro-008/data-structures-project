class Node:
    """Класс для узла очереди"""

    def __init__(self, data):
        """Конструктор класса Node"""
        self.data = data
        self.next_node = None


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        current_node = self.head
        queue_str = ""
        while current_node is not None:
            queue_str += str(current_node.data) + "\n"
            current_node = current_node.next_node
        return queue_str.strip()

    def enqueue(self, data):
        """Метод для добавления элемента в очередь"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass
