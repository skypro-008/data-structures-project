import unittest

from src.linked_list import LinkedList, Node


class TestLinkedList(unittest.TestCase):

    def test_init(self):
        ll = LinkedList()
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning(1)

        self.assertEqual(ll.head.data, 1)
        self.assertEqual(ll.head.next_node, None)
        self.assertEqual(ll.tail.data, 1)
        self.assertEqual(ll.tail.next_node, None)

        old_head = ll.head
        ll.insert_beginning(0)
        self.assertEqual(ll.head.data, 0)
        self.assertEqual(ll.head.next_node, old_head)
        self.assertEqual(ll.tail.data, 1)
        self.assertEqual(ll.tail.next_node, None)

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end(1)

        self.assertEqual(ll.head.data, 1)
        self.assertEqual(ll.head.next_node, None)
        self.assertEqual(ll.tail.data, 1)
        self.assertEqual(ll.tail.next_node, None)

        ll.insert_at_end(2)
        self.assertEqual(ll.head.data, 1)
        self.assertEqual(ll.head.next_node.data, 2)
        self.assertEqual(ll.tail.data, 2)
        self.assertEqual(ll.tail.next_node, None)

    def test_str(self):
        ll = LinkedList()
        self.assertEqual(str(ll), 'None')

        ll.insert_at_end(2)
        self.assertEqual(str(ll), '2 -> None')

        ll.insert_at_end(3)
        ll.insert_beginning(1)
        ll.insert_beginning(0)
        self.assertEqual(str(ll), '0 -> 1 -> 2 -> 3 -> None')

if __name__ == '__main__':
    unittest.main()
