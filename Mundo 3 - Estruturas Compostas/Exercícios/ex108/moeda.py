def moeda(x):
    x = str(x)
    return ('R$'+x)


def metade(x):
    return round((x / 2), 2)


def dobro(x):
    return round((x * 2), 2)


def aumentar(x, porc):
    v = x + (porc / 100) * x
    return round(v, 2)


def reduzir(x, porc):
    v = x - (porc / 100) * x
    return round(v, 2)