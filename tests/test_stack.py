"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import *


class TestStack(unittest.TestCase):
    def test_push(self):
        node_test = Node('test1', None)
        stack_test = Stack()
        stack_test.push(node_test)
        self.assertEqual(node_test, stack_test.top.data)

    def test_pop(self):
        node_test = Node('test1', None)
        stack_test = Stack()
        stack_test.push(node_test)
        sun = stack_test.pop()
        self.assertEqual(sun.data.data, node_test.data)