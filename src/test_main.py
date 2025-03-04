import math
from main import area_circulo  # Importa la función desde tu código

def test_area_circulo_1():
    assert area_circulo(1) == math.pi  # Prueba con radio 1

def test_area_circulo_2():
    assert round(area_circulo(2), 2) == 12.57  # Prueba con radio 2

def test_area_circulo_3():
    assert round(area_circulo(3), 2) == 28.27  # Prueba con radio 3

def test_area_circulo_4():
    assert round(area_circulo(4), 2) == 50.27  # Prueba con radio 4

def test_area_circulo_5():
    assert round(area_circulo(5), 2) == 78.54  # Prueba con radio 5
