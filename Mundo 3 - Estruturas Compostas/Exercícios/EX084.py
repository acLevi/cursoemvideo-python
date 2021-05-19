# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) Uma listagem com as pessoas mais pesadas 
# C) Uma listagem com as pessoas mais leves

# Lists

dados = []
grupo = []

# Variables

cont = 0
pesomaior = pesomenor = 0

# Loop
while True:
    cont += 1
    nome = (str(input('Nome: ')))
    dados.append(nome)
    peso = (float(input('Peso (KG): ')))
    if cont == 1:
        pesomaior = pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
    dados.append(peso)
    grupo.append(dados[:])
    dados.clear()

    # Continue or exit
    answer = 'a'
    while answer[0] not in 'sn':
        answer = str(input('Quer continuar [S/N]? ')).lower().strip()
    if answer[0] == 'n':
        break

# Output

# A)
print()
print('Nomes:', end=' ')
for p in grupo:
    print(p[0], end=', ')
print()
print('Pesos: ', end=' ')
for p in grupo:
    print(p[1], end=', ')
print()
print(f'Foram cadastradas {cont} pessoas.')
print()

# B)

print(f'O maior peso cadastrado foi {pesomaior}kg. Peso de', end=' ')
for p in grupo:
    if p[1] == pesomaior:
        print(p[0], end=' ')
print()

# C)

print(f'O menor peso cadastrado foi {pesomenor}kg. Peso de', end=' ')
for p in grupo:
    if p[1] == pesomenor:
        print(p[0], end=' ')

