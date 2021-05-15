# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# Se o valor 5 foi digitado e está ou não na lista.

numeros = []

# Loop
while True:
    resposta = 'a'
    n = int(input('Digite um número: '))
    numeros.append(n)
    print('Valor adicionado.')
    while resposta[0] not in 'sn':
        resposta = str(input('Quer continuar [S/N]? ')).lower().strip()
    if resposta == 'n':
        break

print(f'Números digitados: {numeros}')
print(35 * '=')
# A)
print(f'Na lista: {numeros}, foram digitados {len(numeros)} números.')
# B)
print(f'Lista ordenada em forma decrescente: {sorted(numeros, reverse=True)}')
# C)
if 5 not in numeros:
    print('O número 5 não foi digitado.')
else:
    print('O número 5 foi digitado e está na lista.')