"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import pytest

from src.linked_list import Node, LinkedList

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


