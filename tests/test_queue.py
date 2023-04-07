"""Здесь надо написать тесты с использованием unittest для модуля queue."""
"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.queue import *


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        node_test = 'test1'
        queue_test = Queue()
        queue_test.enqueue(node_test)
        self.assertEqual(node_test, queue_test.head.data)

    def test_str(self):
        queue_test = Queue()
        node_test1 = 'test1'
        node_test2 = 'test2'
        queue_test.enqueue(node_test1)
        queue_test.enqueue(node_test2)
        self.assertEqual(str(queue_test), "test1\ntest2")