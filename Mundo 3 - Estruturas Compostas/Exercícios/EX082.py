# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

# Definindo as listas
numeros = []
npares = []
nimpares = []

# Loop
while True:
    resposta = 'a'
    numeros.append(int(input('Digite um número: ')))
    while resposta not in 'sn':
        resposta = str(input('Quer continuar [S/N]? ')).lower().strip()
    if resposta[0] == 'n':
        break
# Percorrendo a lista
for num in numeros:
    # Verificando se num é par
    if num % 2 == 0:
        npares.append(num)
    # Caso não, n é ímpar
    else:
        nimpares.append(num)

print(f'Números digitados: {numeros}')
print(f'Números pares da lista: {sorted(npares)}')
print(f'Números ímpares da lista: {sorted(nimpares)}')