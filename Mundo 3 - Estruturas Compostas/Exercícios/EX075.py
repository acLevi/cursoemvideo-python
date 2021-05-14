# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares

# Declarando a tupla
nums = tuple()

# Lendo os quatro números e adcionando na tupla
for c in range(1, 5):
    n = int(input(f'Digite o {c}º número: '))
    nums += (n,)

# a) Quantidade de vezes em que o número 9 apareceu
if 9 in nums:
    print(f'O número 9 aparece {nums.count(9)} vezes na tupla.')
else:
    print('O número não está na tupla.')

# b) Posição do valor 3
if 3 in nums:
    print(f'O número 3 aparece na {nums.index(3) + 1}ª posição da tupla.')
else:
    print('O número 3 não está na tupla')

# c) Números pares
print('Números pares contidos na tupla: ', end='')
for n in nums:
    if n % 2 == 0:
        print(n, end=' ')