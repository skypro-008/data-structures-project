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

    def test_pop_empty_stack(self):
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_pop_single_element_stack(self):
        stack = Stack()
        stack.push(1)
        result = stack.pop()
        self.assertEqual(result, 1)
        self.assertIsNone(stack.top)

    def test_pop_multiple_elements_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        result1 = stack.pop()
        result2 = stack.pop()
        result3 = stack.pop()
        self.assertEqual(result1, 3)
        self.assertEqual(result2, 2)
        self.assertEqual(result3, 1)
        self.assertIsNone(stack.top)

    def test_push_pop_and_str(self):
        stack = Stack()
        stack.push("A")
        stack.push("B")
        stack.push("C")
        stack.pop()
        self.assertEqual(str(stack), "Stack: B -> A -> None")

    def test_empty_stack_str(self):
        stack = Stack()
        self.assertEqual(str(stack), "Stack: None")


if __name__ == '__main__':
    unittest.main()
