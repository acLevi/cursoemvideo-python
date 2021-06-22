# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

turma = []

while True:
    nome = input('Nome: ')
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    m = (n1 + n2) / 2
    turma.append([nome, [n1, n2], m])

    answer = 'a'
    while answer[0] not in 'sn':
        answer = input(('Quer continuar [S/N]? ')).strip().lower()
    if answer[0] == 'n':
        break 

print('-=' * 20)
print(f'{"No.":<5} {"NOME":<20} {"MÉDIA":<2}')
for i, aluno in enumerate(turma):
    print('-' * 40)
    print(f'{i:<5} {aluno[0]:<20} {aluno[2]:<2.1f}')

while True:
    print('-' * 40)
    op = int(input('Digite o número do aluno para mostrar suas notas: '))
    print('-' * 40)
    if op == 999:
        break
    if 0 <= op <= len(turma) - 1:
        print(f'Notas de {turma[op][0]} são {turma[op][1]}')
    