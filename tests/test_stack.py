"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestStack(unittest.TestCase):
    def test_node(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')
        self.assertEqual(n1.next_node, None)
        self.assertEqual(n2.next_node, n1)

    def test_stack(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(stack.top.next_node.data, 'data1')
        self.assertIsNone(stack.top.next_node.next_node)

        with self.assertRaises(AttributeError):
            stack.top.next_node.next_node.data


if __name__ == '__main__':
    unittest.main()