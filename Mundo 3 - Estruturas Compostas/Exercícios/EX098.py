# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada.
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = passo * (-1)

    print('-'*30)
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}')
    sleep(2)

    if inicio < fim:
        c = inicio
        while c <= fim:
            print(c, end=' ', flush=True)
            sleep(0.5)
            c += passo
        print('FIM')
    else:
        c = inicio
        while c >= fim:
            print(c, end=' ', flush=True)
            sleep(0.5)
            c -= passo
        print('FIM')

    print('-'*30)


# main
contador(0, 10, 1)
sleep(1)
contador(10, 0, 2)
sleep(1)
print("Contagem do usuário:")
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)