"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_empty_list(self):
        self.assertEqual(str(self.ll), "None")

    def test_insert_beginning(self):
        self.ll.insert_beginning({'id': 1})
        self.assertEqual(str(self.ll), "{'id': 1} -> None")

        self.ll.insert_beginning({'id': 0})
        self.assertEqual(str(self.ll), "{'id': 0} -> {'id': 1} -> None")

    def test_insert_at_end(self):
        self.ll.insert_at_end({'id': 1})
        self.assertEqual(str(self.ll), "{'id': 1} -> None")

        self.ll.insert_at_end({'id': 2})
        self.assertEqual(str(self.ll), "{'id': 1} -> {'id': 2} -> None")

    def test_insert_beginning_and_end(self):
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.assertEqual(str(self.ll), "{'id': 1} -> {'id': 2} -> None")

        self.ll.insert_beginning({'id': 0})
        self.ll.insert_at_end({'id': 3})
        self.assertEqual(str(self.ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")
