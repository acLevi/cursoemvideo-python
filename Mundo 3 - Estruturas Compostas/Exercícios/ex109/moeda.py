def moeda(x, cif='R$'):
    x = round(x, 2)
    x = str(x).replace('.', ',')
    return (cif+x)


def metade(x, show=False):
    if show:
        return moeda(round((x / 2), 2))
    else:
        return round((x / 2), 2)


def dobro(x, show=False):
    if show:
        return moeda(round((x * 2), 2))
    else:
        return round((x * 2), 2)


def aumentar(x, porc, show=False):
    v = x + (porc / 100) * x
    if show:
        return moeda(round(v, 2))
    else:
        return round(v, 2)


def reduzir(x, porc, show=False):
    v = x - (porc / 100) * x
    if show:
        return moeda(round(v, 2))
    else:
        return round(v, 2)