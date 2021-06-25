# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

dados = []
cadastro = {}
sidade = 0

while True:
    answer = 'x'
    cadastro["nome"] = str(input('Nome: ')).strip().title()
    cadastro["idade"] = int(input('Idade: '))
    sidade += cadastro['idade']
    while True:
        cadastro["sexo"] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if cadastro['sexo'] in 'MF':
            break
    dados.append(cadastro.copy())
    while answer[0] not in 'sn':
        answer = str(input('Quer continuar? ')).strip().lower()
    if 'n' in answer[0]:
        break
print('-='*15)
print(f'A) Foram cadastradas {len(dados)} pessoas.' if len(dados) > 1 else 'Foi cadastrado apenas uma pessoa.')
print(f'B) A média de idade das pessoas cadastradas é {sidade / len(dados)}')
print('C) Lista de pessoas no sexo feminino: ',end='')
for p in dados:
    if p['sexo'] == 'F':
        print(f'[{p["nome"]}]',end=' ')
print()
print(f'D) Lista de pessoas com idade acima da média: ')
for p in dados:
    if p['idade'] > (sidade / len(dados)):
        print(f'    {p["nome"]} com {p["idade"]} anos de idade.')
    else:
        print("     ---")