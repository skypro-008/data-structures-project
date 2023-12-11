"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import pytest

from src.stack import Node, Stack


@pytest.fixture
def test_node():
    return Node(1, 2)


@pytest.fixture
def stack():
    return Stack()


def test_node_init(test_node):
    assert test_node.data == 1
    assert test_node.next_node == 2


def test_stack_init(stack):
    assert stack.top is None


def test_stack_str():
    stack = Stack()
    assert str(stack) == ""
    stack.push("data1")
    assert str(stack) == "data1"
    stack.push("data2")
    assert str(stack) == "data2"
    stack.pop()
    assert str(stack) == "data1"
    stack.pop()
    assert str(stack) == ""


def test_stack_push(stack):
    stack.push("data1")
    stack.push("data2")
    stack.push("data3")
    assert stack.top.data == "data3"
    assert stack.top.next_node.data == "data2"


def test_push_and_pop():
    stack = Stack()
    stack.push("data1")
    stack.push("data2")
    data = stack.pop()
    assert data == "data2"
    data = stack.pop()
    assert data == "data1"


def test_pop_empty_stack():
    stack = Stack()
    data = stack.pop()
    assert data is None
    assert stack.top is None


def test_pop_from_non_empty_stack():
    stack = Stack()
    stack.push("data1")
    data = stack.pop()
    assert data == "data1"
    assert stack.top is None


def test_push_and_pop_multiple_elements():
    stack = Stack()
    stack.push("data1")
    stack.push("data2")
    stack.push("data3")
    data = stack.pop()
    assert data == "data3"
    data = stack.pop()
    assert data == "data2"
    data = stack.pop()
    assert data == "data1"
    assert stack.top is None


def test_str_stack():
    new_stack = Stack()
    assert print(new_stack) is None
