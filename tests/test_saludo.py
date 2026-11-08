import pytest

from src.saludo import saludar


def test_saludo_basico():
    assert saludar("Santiago") == "Hola, Santiago!"


def test_saludo_con_espacios():
    assert saludar("  Ana ") == "Hola, Ana!"


def test_saludo_nombre_vacio():
    with pytest.raises(ValueError):
        saludar("")
