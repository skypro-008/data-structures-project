"""Здесь надо написать тесты с использованием unittest для модуля stack."""


import pytest

from src.stack import Node, Stack

@pytest.fixture
def return_date():
    return Node("Смартфон", 10000)

@pytest.fixture
def return_date1():
    return Stack.push("Смартфон1")

def test_push():
    """Тест для функции пуш стека"""
    Stack.push("Смартфон")
    assert Stack.push() == "Смартфон"


#def test_apply_discount(return_date):
    """Тест для функции расчета цены со скидкой"""
#    return_date.pay_rate = 0.8
#    return_date.apply_discount()
#    assert return_date.price == 8000


def test_init(return_date):
    """Тест для init, просто интересно было, смысла в нем нет"""
    assert return_date.data == 'Смартфон'
    assert return_date.next_node == 10000

