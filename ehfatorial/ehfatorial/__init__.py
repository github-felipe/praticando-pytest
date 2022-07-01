__version__ = '0.1.0'


def e_fatorial(valor):
    from math import factorial
    chave = 0
    while True:
        numero = factorial(chave)
        if numero == valor:
            return True
            break
        elif numero > valor:
            return False
            break
        else:
            chave += 1


def fatorial_doque(valor):
    from ehfatorial.ehfatorial import e_fatorial
    from math import factorial
    if not e_fatorial(valor):
        return 'o valor inserido não é um fatorial'
    elif valor == 1:
        return (0, 1)
    else:
        chave = 2
        while True:
            numero = factorial(chave)
            if numero == valor:
                return chave
            else:
                chave += 1
