"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import pytest

from src.linked_list import Node, LinkedList, NotID


def tests_linked_list():
    """тест для класса LinkedList односвязного списка"""
    new = LinkedList()
    new.insert_beginning({'num1': 1})
    assert str(new) == "{'num1': 1} -> None"
    new.insert_beginning({'num2': 2})
    assert str(new) == "{'num2': 2} -> {'num1': 1} -> None"
    new.insert_at_end({'num3': 3})
    assert str(new) == "{'num2': 2} -> {'num1': 1} -> {'num3': 3} -> None"
    new.remove_first()
    assert str(new) == "{'num1': 1} -> {'num3': 3} -> None"
    new.remove_last()
    assert str(new) == "{'num1': 1} -> None"
    new.remove_first()
    assert str(new) == "None"


def test_insert_invalid_data_type():
    """тест на некоретный ввод не тип словарь"""

    with pytest.raises(TypeError) as e:
        LinkedList.insert_at_end('аеегкегкегкег')
    with pytest.raises(TypeError) as e:
        LinkedList.insert_beginning('аеегкегкегкег')


def test_to_list():
    """тест метода  to_list() на вывод ввиде списка"""
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    lst = ll.to_list()
    assert lst == [{'id': 1, 'username': 'lazzy508509'}]
    ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
    lst = ll.to_list()
    assert lst == [{'id': 1, 'username': 'lazzy508509'}, {'id': 2, 'username': 'mik.roz'}]


def test_get_data_by_id():
    """тест функции get_data_by_id, на вывод словаря с определенным id и в случае если его нет в словаре"""
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
    ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
    ll.insert_beginning({'id': 0, 'username': 'serebro'})
    user_data = ll.get_data_by_id(3)
    assert user_data == {'id': 3, 'username': 'mosh_s'}
    with pytest.raises(NotID) as e:
        ll.get_data_by_id(4)
    assert str(e.value) == "Нет ID в списке."
