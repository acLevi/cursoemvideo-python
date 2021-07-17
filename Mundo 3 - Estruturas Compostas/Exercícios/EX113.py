# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(prompt):
    while True:
        try:
            n = int(input(prompt))
        except (TypeError, ValueError):
            print("Erro. Digite um número inteiro válido.")
            continue
        else:
            return n

def leiaFloat(prompt):
    while True:
        try:
            n = float(input(prompt))
        except (TypeError, ValueError):
            print("Erro. Digite um número real válido.")
            continue
        else:
            return n
    

# main

a = leiaInt("Digite um número inteiro: ")
print(a)
n = leiaFloat("Digite um número real: ")
print(n)