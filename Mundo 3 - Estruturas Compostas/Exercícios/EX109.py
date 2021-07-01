# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from ex109 import moeda

v = float(input('Valor: R$'))
print(f'A metade de {moeda.moeda(v)} é {moeda.metade(v, show=True)}')
print(f'O dobro de {moeda.moeda(v)} é {moeda.dobro(v, show=True)}')
print(f'Aumentando 15%, temos {moeda.aumentar(v, 15, show=True)}')
print(f'Reduzindo 5%, temos {moeda.reduzir(v, 5, show=True)}')