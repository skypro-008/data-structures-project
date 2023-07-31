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

    def test_to_list(self):
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.ll.insert_beginning({'id': 0, 'username': 'serebro'})
        expected_result = [{'id': 0, 'username': 'serebro'},
                           {'id': 1, 'username': 'lazzy508509'},
                           {'id': 2, 'username': 'mik.roz'},
                           {'id': 3, 'username': 'mosh_s'}]
        self.assertEqual(self.ll.to_list(), expected_result)

    def test_get_data_by_id(self):
        self.ll.insert_beginning({'id': 3, 'username': 'mosh_s'})

        # Поиск существующего id
        self.assertEqual(self.ll.get_data_by_id(3), {'id': 3, 'username': 'mosh_s'})
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end('idusername')
        self.ll.insert_at_end([1, 2, 3])
        self.ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
        self.assertEqual(self.ll.get_data_by_id(2), {'id': 2, 'username': 'mosh_s'})

        # Поиск несуществующего id
        self.assertIsNone(self.ll.get_data_by_id(4))

        # Поиск с неподходящим форматом данных
        self.assertIsNone(self.ll.get_data_by_id("wrong_id"))
