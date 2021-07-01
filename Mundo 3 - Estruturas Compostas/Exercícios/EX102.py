# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado o fatorial
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial do valor n.
    """
    
    f = 1
    for c in range(num, 0, -1):
        if show == True:
            if c > 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} =', end=' ')
        f *= c
    return f

n = int(input('Digite um número para mostrar seu fatorial: '))
print(fatorial(n, True))