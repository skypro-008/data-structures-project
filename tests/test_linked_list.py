"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest

from src.linked_list import LinkedList


class Teststack(unittest.TestCase):

    def test_node(self):
        ll = LinkedList()

        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})

        print(str(ll))
        assert str(ll) == " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"

    def test_linked_list(self):
        ll = LinkedList()

        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})

        lst = ll.to_list()

        assert lst[0] == "{'id': 0, 'username': 'serebro'}"
        assert lst[1] == "{'id': 1, 'username': 'lazzy508509'}"
        assert lst[2] == "{'id': 2, 'username': 'mik.roz'}"
        assert lst[3] == "{'id': 3, 'username': 'mosh_s'}"

        user_data = ll.get_data_by_id(3)
        assert user_data == {'id': 3, 'username': 'mosh_s'}

        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end('idusername')
        ll.insert_at_end([1, 2, 3])
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

        user_data = ll.get_data_by_id(2)
        print(user_data)
