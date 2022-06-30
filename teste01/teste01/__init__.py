__version__ = '0.1.0'


def numero_meio(valor):
    comprimento = len(str(valor))
    valor = str(valor)
    metade_comprimento = comprimento / 2
    if comprimento % 2 == 1:
        metade_comprimento = int(metade_comprimento - 0.5)
        valor_meio = valor[metade_comprimento]
        return str(valor_meio)
    else:
        metade_comprimento = int(metade_comprimento)
        valores_meio = f'{valor[metade_comprimento -1]}, {valor[metade_comprimento]}'
        return valores_meio
