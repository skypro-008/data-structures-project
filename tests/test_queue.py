"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue


class NodeTestCase(unittest.TestCase):
    def test_node_creation(self):
        data = 'data'
        node = Node(data)
        self.assertEqual(node.data, data)
        self.assertIsNone(node.next_node)


class QueueTestCase(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_queue_empty_str(self):
        self.assertEqual(str(self.queue), "")

    def test_enqueue_single_element(self):
        data = 'data'
        self.queue.enqueue(data)
        self.assertEqual(str(self.queue), data)
        self.assertEqual(self.queue.head.data, data)
        self.assertEqual(self.queue.tail.data, data)
        self.assertIsNone(self.queue.tail.next_node)

    def test_enqueue_multiple_elements(self):
        data1 = 'data1'
        data2 = 'data2'
        data3 = 'data3'
        self.queue.enqueue(data1)
        self.queue.enqueue(data2)
        self.queue.enqueue(data3)
        expected_str = data1 + "\n" + data2 + "\n" + data3
        self.assertEqual(str(self.queue), expected_str)
        self.assertEqual(self.queue.head.data, data1)
        self.assertEqual(self.queue.head.next_node.data, data2)
        self.assertEqual(self.queue.tail.data, data3)
        self.assertIsNone(self.queue.tail.next_node)

if __name__ == '__main__':
    unittest.main()
