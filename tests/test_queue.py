"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import pytest

from src.queue import Node, Queue


def test_stack():
    """ Добавляем два элемента в стек и затем извлекаем их"""
    queue = Queue()
    queue.data = []

    queue.enqueue('one')
    queue.enqueue('two')

    assert queue.dequeue() == 'one'
    assert queue.dequeue() == 'two'


def test_str():
    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    assert str(queue) == "data1\ndata2\ndata3"

    queue1 = Queue()
    assert str(queue1) == ""