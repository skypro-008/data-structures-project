"""Здесь надо написать тесты с использованием unittest для модуля stack."""

import pytest

from src.stack import Node, Stack


@pytest.fixture
def return_date():
    return Node("Смартфон", 10000)


def test_init(return_date):
    """Тест для init, просто интересно было, смысла в нем нет"""
    assert return_date.data == 'Смартфон'
    assert return_date.next_node == 10000


def test_stack():
    """ Добавляем два элемента в стек и затем извлекаем их"""
    stack = Stack()
    stack.data = []

    stack.push('one')
    stack.push('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'

def test_str():
    """тест метода __str__"""
    stack = Stack()
    stack.push('one')
    stack.push('two')
    assert str(stack) == "['one', 'two']"
    stack.pop()
    assert str(stack) == "['one']"
