"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest

from src.linked_list import Node, LinkedList


class NodeTest(unittest.TestCase):

    def test_init(self):
        node = Node()
        self.assertIsNone(node.data)
        self.assertIsNone(node.next_node)


class LinkedListTest(unittest.TestCase):

    def test_init(self):
        ll = LinkedList()
        self.assertIsNone(ll.head)

    def test_insert_beginning(self):
        ll = LinkedList()
        self.assertIsNone(ll.head)

        ll.insert_beginning({'id': 1})
        self.assertTrue(ll.head)

    def test_insert_at_end(self):
        ll = LinkedList()
        self.assertIsNone(ll.head)

        ll.insert_at_end({'id': 1})
        ll.insert_at_end({'id': 2})
        self.assertTrue(ll.head)
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.head.next_node.data, {'id': 2})

    def test_str(self):
        ll = LinkedList()
        self.assertIsNone(ll.head)
        ll.insert_at_end({'id': 1})
        self.assertEqual(ll.__str__(), "{'id': 1} -> None")

    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.assertEqual(ll.to_list(), [{'id': 1, 'username': 'lazzy508509'}, {'id': 2, 'username': 'mik.roz'}])

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.assertEqual(ll.get_data_by_id(1), {'id': 1, 'username': 'lazzy508509'})
