from teste01 import __version__
from pytest import mark
from teste01 import numero_meio


def test_version():
    assert __version__ == '0.1.0'


@mark.parametrize(
    'parametro, resultado_esperado',
    [(43791287, '9, 1'), (432, '3'), (3, '3'), (49, '4, 9'), (2984758092427093847, '2')]
)
def test_qual_e_o_numero_do_meio(parametro, resultado_esperado):
    assert numero_meio(parametro) == resultado_esperado
