# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

nums = []

def sorteia(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        lst.append(randint(0,10))
    print(lst)

def somapar(lst):
    spar = 0
    for n in nums:
        if n % 2 == 0:
            spar += n
    print(f'Somando os valores par de {lst}, temos {spar}')


sorteia(nums)
somapar(nums)