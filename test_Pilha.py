from pilha import Pilha
import pytest


@pytest.fixture
def before():
    s = Pilha()
    return s


def test_vazio(before):
    assert before.isEmpty() == True


def test_adicionando():
    s = Pilha()
    s.push(2)
    assert 2 in s
