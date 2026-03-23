from cantina import calcular_total, validar_pedido

def test_calcular_total():
    assert calcular_total(2, 5) == 10


def test_calcular_total_zero():
    assert calcular_total(0, 10) == 0

