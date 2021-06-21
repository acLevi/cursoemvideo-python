# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Pop matriz; First columns 1-3 of row L

for l in range(0, 3):
    for c in range(0, 3):
        x = int(input(f'Digite um número para a posição [{l+1}, {c+1}]: '))
        matriz[l][c] = x

# Display matrix

for n in matriz:
    for i in range(0,3):
        print(f'[ {n[i]:^3} ]', end=' ')
    print()