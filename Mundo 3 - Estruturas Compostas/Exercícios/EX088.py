# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

qnt = int(input('Quantidade de jogos a sortear: '))

print(f'-=-= SORTEANDO {qnt} JOGO =-=-' if qnt == 1 else f'-=-= SORTEANDO {qnt} JOGOS =-=-')

jogo = []
nums = []

# enquanto 'jogo' não estiver com 'qnt' de jogos
while len(jogo) < qnt:
    # enquanto 'nums' não estiver com 6 valores
    while len(nums) <= 6:
        # gerando um randint novo a cada repetição
        r = randint(1,60)
        # se r não estiver em nums
        if nums.count(r) < 1:
            # adiciona-se r a nums
            nums.append(r)
    nums.sort()
    jogo.append(nums[:])
    nums.clear()

for c in range(0, qnt):
    print(f'Jogo {c+1}: {jogo[c]}')
    sleep(1)

