import calculando
import pytest

#-----------Fixture-------------------
@pytest.fixture
def numero():
    x = 10
    y = 5
    return [x, y]

def test_numero(numero):
    assert 10 == numero[0]


#------------------Mark----------------------
def test_add():
    assert calculando.add(5,5) == 10, "deveria ser 10"

#mark customizado. Posso rodar so esse teste 
@pytest.mark.produto 
def test_product():
    assert calculando.product(10,1) == 10

#--------------------Assert----------------------
def test_nome():
    x = "ola"
    assert 'o' in x
   
