from random import randint
from time import sleep
from operator import itemgetter



valores = { 'jogador 1' : randint(1,6), 'jogador 2' : randint(1,6), 
'jogador 3' : randint(1,6), 'jogador 4' : randint(1,6) }

ranking = list()

print('Valores sorteados:')
for k, v in valores.items():
    print(f'    O {k} tirou {v}')
    sleep(1)

print('Ranking do jogadores:')

ranking = sorted(valores.items(), key=itemgetter(1),reverse=True)

for r, v in enumerate(ranking):
    print(f'    {r+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)