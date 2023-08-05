"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import pytest


def test_enqueue(queue):
    assert queue.head.data == 'data1'
    assert queue.head.next_node.data == 'data2'
    assert queue.tail.data == 'data3'
    assert queue.tail.next_node is None
    with pytest.raises(AttributeError):
        print(queue.tail.next_node.data)


def test_dequeue(queue):
    assert queue.dequeue() == 'data1'
    assert queue.tail.data == 'data3'
    assert queue.dequeue() == 'data2'
    assert queue.tail.data == 'data3'
    assert queue.dequeue() == 'data3'
    assert queue.tail.data == 'data3'
    with pytest.raises(AttributeError):
        assert queue.dequeue()


def test_str(queue):
    assert str(queue) == "data1\ndata2\ndata3"
    queue.enqueue(123)
    assert str(queue) == "data1\ndata2\ndata3\n123"
