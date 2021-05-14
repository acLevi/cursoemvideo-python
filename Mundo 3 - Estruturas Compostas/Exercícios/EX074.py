# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

# Importando a funçao randint da biblioteca random
from random import randint

# Declarando a tupla com os comandos randint
nums = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0 ,10))

# Encontrando o maior e menor número da tupla

# Método 01
maior = max(nums)
menor = min(nums)

# Método 02
# maior = sorted(nums)[-1]
# menor = sorted(nums)[0]

print(f'Números sorteados: {nums}')
print(f'Maior número sorteado: {maior}')
print(f'Menor número sorteado: {menor}')