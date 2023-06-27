import pytest
from src import queue


@pytest.fixture()
def node1():
    return queue.Node(5, None)


@pytest.fixture()
def node2(node1):
    return queue.Node('a', node1)


@pytest.fixture()
def empty_queue():
    return queue.Queue()


def test_node_init(node1, node2):
    assert node1.data == 5
    assert node2.next_node == node1


def test_queue_init(empty_queue):
    assert empty_queue.head is None
    assert empty_queue.tail is None


def test_queue_enqueue(empty_queue):
    empty_queue.enqueue('data1')
    empty_queue.enqueue('data2')
    empty_queue.enqueue('data3')
    assert empty_queue.head.data == 'data1'
    assert empty_queue.head.next_node.data == 'data2'
    assert empty_queue.tail.data == 'data3'
    assert empty_queue.tail.next_node is None


def test_queue_str(empty_queue):
    assert str(empty_queue) == ""
    empty_queue.enqueue('data1')
    empty_queue.enqueue('data2')
    empty_queue.enqueue('data3')
    assert str(empty_queue) == """data1\ndata2\ndata3"""
