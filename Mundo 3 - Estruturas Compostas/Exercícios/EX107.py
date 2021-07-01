# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

from ex107 import moeda

v = float(input('Valor: '))
pa = float(input('Aumento (%): '))
pr = float(input('Redução (%): '))
print(f'''
A metade {v} é {moeda.metade(v)}.
O dobro de {v} é {moeda.dobro(v)}.
Aumentando {pa}%, temos {moeda.aumentar(v, pa)}.
Reduzindo {pr}%, temos {moeda.reduzir(v, pr)}''')
