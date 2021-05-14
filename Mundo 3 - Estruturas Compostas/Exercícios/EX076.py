# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# Tupla
produtos = ('GTX 1660', 3999, 'GTX 1650', 3499, 'GTX 1030', 669, 'RTX 3070', 11999, 'GT 710', 323, 'Radeon 6570', 499, 'Radeon HD5450', 249, 'GeForce G210', 289, 'GTX750 Ti', 1299, 'GT740', 749, 'RTX 3060', 6889)

# Lista de preços
print(f'{"PREÇOS":^35}')
print('=' * 35)
for pos, p in enumerate(produtos):
    if pos % 2 == 0:
        print(f'{p:.<20}', end=' ')
    else:
        print(f'R${p:>10.2f}')
print('=' * 35)
