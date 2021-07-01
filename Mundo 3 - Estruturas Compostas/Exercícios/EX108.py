# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

from ex108 import moeda

v = float(input('Valor: R$'))
pa = int(input('Aumento (%): '))
pr = int(input('Redução (%): '))
print(f'''A metade de {moeda.moeda(v)} é {moeda.moeda(moeda.metade(v))}.
O dobro de {moeda.moeda(v)} é {moeda.moeda(moeda.dobro(v))}.
Aumentando {(pa)}%, temos {moeda.moeda(moeda.aumentar(v, pa))}.
Reduzindo {(pr)}%, temos {moeda.moeda(moeda.reduzir(v, pr))}''')
