import unittest
from src.queue import Queue

"""Здесь надо написать тесты с использованием unittest для модуля queue."""

class QueueTest(unittest.TestCase):

    def test_init(self):
        queue = Queue()
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')
        self.assertIsNone(queue.tail.next_node)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        data = queue.dequeue()
        self.assertEqual(data, 'data1')
        self.assertEqual(queue.head.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')

        data = queue.dequeue()
        self.assertEqual(data, 'data2')
        self.assertEqual(queue.head.data, 'data3')
        self.assertEqual(queue.tail.data, 'data3')


