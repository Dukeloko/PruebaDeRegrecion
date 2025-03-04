import math

def area_circulo(radio):
    return math.pi * radio ** 2  # Usar math.pi para mayor precisión

def test_area():
    assert area_circulo(1) == math.pi  # Compara con el valor correcto de π
    assert round(area_circulo(2), 2) == 12.57  # Redondeo para evitar errores de precisión
    assert round(area_circulo(3), 2) == 28.27
