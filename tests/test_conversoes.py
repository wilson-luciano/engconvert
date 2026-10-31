"""Sprint 08 — testes das funções reais da Aula 08.1."""

import pytest

from engconvert.conversoes import converter, converter_temperatura, obter_unidades
from engconvert.dados import grandezas, unidades_temperatura


@pytest.mark.parametrize(
    "valor, grandeza, origem, destino, esperado",
    [
        (1, "Pressão", "bar", "kPa", 100),
        (1, "Pressão", "atm", "Pa", 101325),
        (1, "Comprimento", "m", "mm", 1000),
        (12, "Comprimento", "in", "ft", 1),
        (1, "Área", "m²", "cm²", 10000),
        (1, "Área", "ft²", "m²", 0.09290304),
        (1, "Volume", "L", "mL", 1000),
        (1, "Volume", "gal (US)", "L", 3.785411784),
        (1, "Volume", "gal (UK)", "L", 4.54609),
        (0, "Temperatura", "°C", "°F", 32),
        (0, "Temperatura", "°C", "K", 273.15),
        (273.15, "Temperatura", "K", "°C", 0),
        (491.67, "Temperatura", "°R", "°F", 32),
        (32, "Temperatura", "°F", "°R", 491.67),
    ],
)
def test_conversoes_conhecidas(valor, grandeza, origem, destino, esperado):
    resultado = converter(valor, grandeza, origem, destino)
    assert resultado == pytest.approx(esperado, rel=1e-9, abs=1e-9)


@pytest.mark.parametrize("grandeza", ["Pressão", "Comprimento", "Área", "Volume"])
def test_conversao_identidade(grandeza):
    unidade = next(iter(grandezas[grandeza]))
    assert converter(123.45, grandeza, unidade, unidade) == pytest.approx(123.45)


def test_temperatura_identidade():
    assert converter_temperatura(25, "°C", "°C") == pytest.approx(25)


def test_obter_unidades_pressao():
    assert obter_unidades("Pressão") == list(grandezas["Pressão"].keys())


def test_obter_unidades_temperatura():
    assert obter_unidades("Temperatura") == unidades_temperatura


def test_temperatura_absoluta_rankine_kelvin():
    assert converter(540, "Temperatura", "°R", "K") == pytest.approx(300)
