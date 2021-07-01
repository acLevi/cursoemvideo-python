


def resumo(x, a, r):
    def moeda(x, cif='R$'):
        x = round(x, 2)
        x = str(x).replace('.', ',')
        return (cif+x)


    def metade(x):
        return moeda(round((x / 2), 2))


    def dobro(x):
        return moeda(round((x * 2), 2))

    aum = a
    def aumentar(x, a):
        v = x + (a / 100) * x
        return moeda(round(v, 2))

    red = r
    def reduzir(x, r):
        v = x - (r / 100) * x
        return moeda(round(v, 2))

    print('-'*20)
    print(' '* 6,'RESUMO')
    print('-'*20)
    print(f'Preço analisado: {moeda(x):>3}')
    print(f'Dobro do preço: {dobro(x):>4}')
    print(f'Metade do preço: {metade(x):>4}')
    print(f'{a}% de Aumento: {aumentar(x, a):>3}')
    print(f'{r}% de redução: {reduzir(x, r):>3}')