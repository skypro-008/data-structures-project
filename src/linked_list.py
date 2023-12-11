class Node:
    """Класс для узла односвязного списка"""

    pass


class LinkedList:
    """Класс для односвязного списка"""

    def insert_beginning(self, data: dict) -> None:
        pass

    def insert_at_end(self, data: dict) -> None:
        pass

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ""
        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node

        ll_string += " None"
        return ll_string
