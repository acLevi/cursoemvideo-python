# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['nome'] = str(input('Nome: ')).strip().title()
aluno['média'] = float(input('Média: '))
aluno['situação'] = 'Aprovado' if aluno['média'] >= 7.0 else 'Reprovado'

print('-='*15)

print(f'Nome: {aluno["nome"]}')
print(f'Média: {aluno["média"]}')
print(f'Situação: {aluno["situação"]}')