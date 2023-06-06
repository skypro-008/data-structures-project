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

    def setUp(self):
        self.stack = Stack()
        self.stack.push('data1')
        self.stack.push('data2')
        self.stack.push('data3')
        self.stack.push('data4')

    def test_str(self):
        expected_output = "data4 -> data3 -> data2 -> data1 -> "
        self.assertEqual(str(self.stack), expected_output)

    def test_str_recursive(self):
        current_node = self.stack.top
        expected_output = "data4 -> data3 -> data2 -> data1 -> "
        self.assertEqual(self.stack._str_recursive(current_node), expected_output)

    def test_stack_push(self):

        self.assertEqual(self.stack.top.data, 'data4')
        self.assertEqual(self.stack.top.next_node.data, 'data3')
        self.assertEqual(self.stack.top.next_node.next_node.data, 'data2')
        self.assertEqual(self.stack.top.next_node.next_node.next_node.data, 'data1')
        self.assertIsNone(self.stack.top.next_node.next_node.next_node.next_node)

    def test_stack_push_single(self):
        stack = Stack()
        stack.push('data')
        self.assertEqual(stack.top.data, 'data')
        self.assertIsNone(stack.top.next_node)

    def test_pop_non_empty_stack(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')

        data = stack.pop()
        self.assertEqual(data, 'data2')
        self.assertEqual(stack.top.data, 'data1')

        data = stack.pop()
        self.assertEqual(data, 'data1')
        self.assertIsNone(stack.top)




if __name__ == '__main__':
    unittest.main()
