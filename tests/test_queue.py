import pytest
from src import queue


def test_node():
    n2 = queue.Node(10, None)
    n1 = queue.Node("hello", n2)

    assert n1.data == "hello"
    assert n2.data == 10
    assert n1.next_node == n2
