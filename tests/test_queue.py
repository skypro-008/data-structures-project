"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue


class TestQueue(unittest.TestCase):
    def test_node(self):
        n2 = Node('a', None)
        n1 = Node(5, n2)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')
        self.assertEqual(n2.next_node, None)
        self.assertEqual(n1.next_node, n2)

    def test_enqueue(self):
        queue = Queue()
        self.assertIsNone(queue.tail)
        self.assertIsNone(queue.head)

        queue.enqueue('data1')
        self.assertEqual(queue.tail, queue.head)
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node, None)

        queue.enqueue('data2')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.head.next_node.next_node, None)

    def test_str(self):
        queue = Queue()
        self.assertEqual(str(queue), '')

        queue.enqueue('data1')
        self.assertEqual(str(queue), 'data1')

        queue.enqueue('data2')
        self.assertEqual(str(queue), 'data1\ndata2')


if __name__ == '__main__':
    unittest.main()