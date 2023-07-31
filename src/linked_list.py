class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data) -> None:
        """Принимает данные и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data) -> None:
        """Принимает данные и добавляет узел с этими данными в конец связанного списка"""
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
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self):
        """Возвращает список с данными, содержащимися в односвязном списке LinkedList"""
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next_node
        return result

    def get_data_by_id(self, target_id):
        """Возвращает первый найденный в LinkedList словарь с ключом 'id',
        значение которого равно переданному в метод значению"""
        try:
            self.target_id = int(target_id)
        except (TypeError, ValueError):
            print("Ошибка: Неподходящий формат данных. Ожидается числовое значение 'id'.")
            return None
        current_node = self.head
        while current_node:
            if isinstance(current_node.data, dict) and 'id' in current_node.data \
                    and current_node.data['id'] == target_id:
                return current_node.data
            current_node = current_node.next_node
        print(f"Запись с 'id' = {target_id} не найдена.")
        return None
