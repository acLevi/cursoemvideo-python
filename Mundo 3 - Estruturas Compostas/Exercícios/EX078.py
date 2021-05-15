# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# Declarando a lista
numeros = []

# Lendo os valores
for n in range(1, 6):
    numeros.append(int(input(f'Digite um valor para a posição {n}: ')))

# Exibindo as informações
print(f'Valores digitados: {numeros}')
maior = max(numeros)
menor = min(numeros)
print(f'Maior valor da lista: {maior} - Posição:', end=' ')
# Posição do maior
for pos, n in enumerate(numeros):
    if n == maior:
        print(f'{pos + 1}º', end=' ')
print()
# Posição do menor
print(f'Menor valor da lista: {menor} - Posição:', end=' ')
for pos, n in enumerate(numeros):
    if n == menor:
        print(f'{pos + 1}º', end=' ')
print()
