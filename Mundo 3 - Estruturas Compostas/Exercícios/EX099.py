# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(*nums):
    maior = 0
    print('-'*30)
    print('Analisando os valores passados...')
    for n in nums:
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
        if n > maior:
            maior = n
    sleep(0.5)
    print(f'Foram informados {len(nums)} números ao todo.')
    print(f'O maior analisado foi {maior}')
    sleep(1)

maior(4, 5, 6, 7)
maior(1, 3, 7)
maior(9, 3)
maior(12)
maior()
