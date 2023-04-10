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