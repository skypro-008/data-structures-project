from src.queue import Queue

if __name__ == '__main__':
    queue = Queue()

    # Магический метод __str__ возвращает пустую строку
    assert str(Queue()) == ""

    # Добавляем данных в очередь
    queue.enqueue('data1')
    queue.enqueue(None)
    queue.enqueue('data3')
    queue.enqueue('data4')

    # Проверяем очередность хранения данных
    # assert queue.head.data == None
    # assert queue.head.next_node.data == 'data2'
    # assert queue.tail.data == 'data3'
    # assert queue.tail.next_node is None
    # print(queue.tail.next_node.data)  # AttributeError: 'NoneType' object has no attribute 'data'
    # Проверяем магический метод __str__
    # assert str(queue) == "data1\nNone\ndata3"
    print(str(queue))
