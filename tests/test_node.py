from src.node import Node


def test_node():
    """Тестирование класса Node."""
    first = Node(1, None)
    second = Node(2, first)
    assert first.data == 1
    assert second.data == 2
    assert first.next_node is None
