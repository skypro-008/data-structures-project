"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class StackTestCase(unittest.TestCase):
    def test_node_creation(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')
        self.assertIsNone(n1.next_node)
        self.assertEqual(n2.next_node, n1)

    def test_stack_push(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(stack.top.data, 'data3')
        self.assertEqual(stack.top.next_node.data, 'data2')
        self.assertEqual(stack.top.next_node.next_node.data, 'data1')
        self.assertIsNone(stack.top.next_node.next_node.next_node)

    def test_stack_push_single(self):
        stack = Stack()
        stack.push('data')
        self.assertEqual(stack.top.data, 'data')
        self.assertIsNone(stack.top.next_node)


if __name__ == '__main__':
    unittest.main()
