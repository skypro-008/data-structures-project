"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Node, Stack


def test_node():
    n1 = Node(5, None)
    n2 = Node('a', n1)
    assert n1.data == 5, "Неверно сохранены данные node"
    assert n2.data == 'a', "Неверно сохранены данные node"
    assert n2.next_node == n1, "Неверно сохранена ссылка на следующую вершину"


def test_stack():
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    assert stack.top.data == "data3", "Неверно сохранён верхний элемент стека"
    assert stack.top.next_node.next_node.data == "data1", "Неверно сохранена последовательность стека"
    assert stack.top.next_node.next_node.next_node is None


def test_pop():
    stack = Stack()
    stack.push('data1')
    data = stack.pop()

    # стек стал пустой
    assert stack.top is None

    # pop() удаляет элемент и возвращает данные удаленного элемента
    assert data == 'data1'

    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    data = stack.pop()

    # теперь последний элемента содержит данные data1
    assert stack.top.data == 'data1'

    # данные удаленного элемента
    assert data == 'data2'
