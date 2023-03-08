"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.n1 = Node(5, None)
        self.n2 = Node('a', self.n1)
        self.stack = Stack()
        self.stack.push('data1')
        self.stack.push('data2')
        self.stack.push('data3')

    def test_node(self):
        self.assertEqual(self.n1.data, 5)
        self.assertEqual(self.n2.data, 'a')
        self.assertIs(self.n1, self.n2.next_node)

    def test_stack(self):
        self.assertEqual(self.stack.top.data, 'data3')
        self.assertEqual(self.stack.top.next_node.data, 'data2')
        self.assertEqual(self.stack.top.next_node.next_node.data, 'data1')
        self.assertIs(self.stack.top.next_node.next_node.next_node, None)

        with self.assertRaises(AttributeError):
            self.stack.top.next_node.next_node.next_node.data


if __name__ == '__main__':
    unittest.main()
