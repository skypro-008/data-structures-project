import pytest
from src import stack


@pytest.fixture()
def node1():
    return stack.Node(5, None)


@pytest.fixture()
def node2(node1):
    return stack.Node('a', node1)


@pytest.fixture()
def empty_stack():
    return stack.Stack()


def test_node_init(node1, node2):
    assert node1.data == 5
    assert node2.data == 'a'


def test_stack_init(empty_stack):
    assert empty_stack.top is None


def test_stack_push(empty_stack):
    empty_stack.push('data1')
    assert empty_stack.top.data == 'data1'

    empty_stack.push('data2')
    assert empty_stack.top.data == 'data2'


def test_stack_pop(empty_stack):
    empty_stack.push('data1')
    empty_stack.push('data2')
    assert empty_stack.pop() == 'data2'
