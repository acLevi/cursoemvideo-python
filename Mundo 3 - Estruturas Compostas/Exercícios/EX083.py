# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

qparent = 0
expr = str(input('Digite uma expressão: '))
for letra in expr:
    if letra == '(':
        qparent += 1
    if letra == ')':
        qparent -= 1
if qparent == 0:
    print('A expressão é válida.')
else:
    print('A expressão é inválida.')