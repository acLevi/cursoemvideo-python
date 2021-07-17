# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(prompt):
    x = input(prompt)
    while x.isnumeric() == False:
        if x.isnumeric():
            break
        else:
            print('ERRO! Digite um número inteiro válido.')
            x = input(prompt)
    return x

#main
n = leiaInt('Digite um número: ')
print(n)