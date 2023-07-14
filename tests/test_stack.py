"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack

class StackTest(unittest.TestCase):
    def test_push_single_element(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.top.data, 1)
        self.assertIsNone(stack.top.next_node)

    def test_push_multiple_elements(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.top.data, 3)
        self.assertEqual(stack.top.next_node.data, 2)
        self.assertEqual(stack.top.next_node.next_node.data, 1)
        self.assertIsNone(stack.top.next_node.next_node.next_node)

if __name__ == '__main__':
    unittest.main()