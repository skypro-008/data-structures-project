import pytest

from src.linked_list import LinkedList
from src.queue import Queue
from src.stack import Stack


@pytest.fixture
def stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    return s


@pytest.fixture
def queue():
    q = Queue()
    q.enqueue('data1')
    q.enqueue('data2')
    q.enqueue('data3')
    return q


@pytest.fixture
def ll_1():
    ll = LinkedList()
    ll.insert_beginning({'id': 1})
    ll.insert_at_end({'id': 2})
    ll.insert_at_end({'id': 3})
    ll.insert_beginning({'id': 0})
    return ll


@pytest.fixture
def ll_2():
    ll = LinkedList()
    ll.insert_at_end({'id': 1})
    ll.insert_at_end({'id': 2})
    ll.insert_beginning({'id': 0})
    return ll
