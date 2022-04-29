def es_par(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return True
    else:
        return False

def test_positive():
    resultado = es_par(2,4)
    assert resultado , "Los numeros no son pares"

def test_negative():
    resultado = es_par(3,9)
    assert not resultado, "Los numeros son pares"


#-----------------------------#

def test_example():
    result = es_par(5,10)
    assert not result

