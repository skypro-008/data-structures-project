"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node


class Teststack(unittest.TestCase):

    def test_stack(self):
        first = Node(5, None)
        self.assertEqual(first.data, 5)


if __name__ == '__main__':
    unittest.main()
