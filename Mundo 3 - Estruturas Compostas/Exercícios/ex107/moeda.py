def metade(x):
    return round((x / 2), 1)


def dobro(x):
    return round((x * 2), 1)


def aumentar(x, porc):
    v = x + (porc / 100) * x
    return round(v, 1)


def reduzir(x, porc):
    v = x - (porc / 100) * x
    return round(v)