import unittest
from src.stack import Node, Stack
"""Здесь надо написать тесты с использованием unittest для модуля stack."""

class StackTest(unittest.TestCase):
    stack = Stack()
    def test_push(self):
      stack = Stack()
      stack.push('data1')
      stack.push('data2')
      stack.push('data3')
      self.assertEqual(stack.top.data, 'data3')
      self.assertEqual(stack.top.next_node.data, 'data2')
      self.assertEqual(stack.top.next_node.next_node.data, 'data1')

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        data = stack.pop()
        self.assertEqual(data, 'data3')
        self.assertEqual(stack.top.data, 'data2')
        data = stack.pop()
        self.assertEqual(data, 'data2')
        self.assertEqual(stack.top.data, 'data1')
        data = stack.pop()
        self.assertEqual(data, 'data1')




