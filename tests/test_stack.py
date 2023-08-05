"""Здесь надо написать тесты с использованием unittest для модуля stack."""


def test_push(stack):
    assert stack.top.data == 3
    assert stack.top.next_node.data == 2
    assert stack.top.next_node.next_node.data == 1
    assert stack.top.next_node.next_node.next_node is None


def test_pop(stack):
    assert stack.pop() == 3
    assert stack.top.data == 2
    assert stack.pop() == 2
    assert stack.top.data == 1
    assert stack.pop() == 1
    assert stack.top is None


def test_str(stack):
    assert str(stack) == 'Stack. Количество элементов - 3'
    stack.push(4)
    assert str(stack) == 'Stack. Количество элементов - 4'
    stack.pop()
