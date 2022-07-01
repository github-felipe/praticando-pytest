from pytest import mark
from ehfatorial.ehfatorial import e_fatorial, fatorial_doque
from math import factorial


@mark.parametrize(
    'parametro, resultado_esperado', 
    [(1, True), (2, True), (3, False), (6, True), (12, False), (97, False)]
)
def test_e_fatorial_retorna_se_o_numero_e_fatorial_de_outro(parametro, resultado_esperado):
    assert e_fatorial(parametro) == resultado_esperado


@mark.parametrize(
    'parametro',
    [2, 3, 4, 6, 8, 15, 23]
)
def test_fatorial_doque_retorna_de_qual_numero_e_aquele_fatorial(parametro):
    fatorado = factorial(parametro)
    assert fatorial_doque(fatorado) == parametro

