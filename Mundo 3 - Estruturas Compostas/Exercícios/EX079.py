# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Declarando a lista
numeros = []

# Repetição e salvando os números na lista
while True:
    resposta = 'a'
    n = int(input('Digite um valor: '))
    if numeros.count(n) < 1:
        numeros.append(n)
    else:
        print(f'O número {n} já existe na lista.')
    while resposta[0] not in 'sn':
        resposta = str(input('Quer continuar [S/N]? ')).lower().strip()
    if resposta[0] == 'n':
        break
# Exibindo a lista ordenada
print(f'Números ordenados: {sorted(numeros)}')
