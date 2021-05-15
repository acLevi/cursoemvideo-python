# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

from random import randint

# Lista
numeros = []

# Laço para cadastrar os números
for c in range(0, 5):
    print(numeros)
    n = randint(0, 10)
# Se o número digitado for o primeiro, apenas irá adiciona-lo na lista.
    if c == 0:
        numeros.append(n)
        print(f'Número {n} adicionado na lista.')
    # Se não, o programa irá verificar se o n é maior ou menor do que o n da lista e adiciona-lo na posição correta.
    else:
        if n <= numeros[0]:
            numeros.insert(0, n)
            print(f'Número {n} adicionado no ínicio da lista.')
        elif n >= numeros[-1]:
            numeros.append(n)
            print(f'Número {n} adicionado no fim da lista.')
        # Caso as condições anteriores não sejam cumpridas, logicamente o novo n digitado não é maior do que último da lista e nem menor do que o primeiro da lista, ou seja, número ficará entre o primeiro e último.
        else:
            # Se só existerem dois termos na lista (primeiro e último), o n será adicionado entre eles.
            if len(numeros) == 2:
                numeros.insert(1, n)
                print('Número adcionado na posição 2.')
            # Se a condição não for cumprida, isso índicara que já existem 3 termos na lista (primeiro, meio e último), ou seja, o programa terá que verificar se o novo n deve ficar entre primeiro-meio ou meio-último.
            elif len(numeros) == 3:
                # Se n for maior do que o meio, ele ficará entre o ultimo.
                if n >= numeros[1]:
                    numeros.insert(2, n)
                    print('Número adicionado na poisção 3.')
                # Se não, n ficará antes do meio.
                else:
                    numeros.insert(1, n)
                    print('Número adicionado na posição 2.')
            # Caso nenhuma das condições anteriores forem cumpridas, isso indicará que exitem 4 termos na lista e que o novo n terá que ficar no meio ou entre primeiro-segundo ou terceiro-quarto
            else:
                # Se n ficará no meio[2]
                if numeros[1] <= n <= numeros[2]:
                    numeros.insert(2, n)
                    print('Número adicionado na posição 3.')
                # Se não, n deverá ficar entre o primeiro-segundo ou terceiro-quarto
                else:
                    # Caso n fique entre o primeiro-segundo
                    if numeros[0] <= n <= numeros[1]:
                        numeros.insert(1, n)
                        print('Número adicionado na posição 2.')
                    # Se não, logicamente, n ficará entre terceiro-quarto
                    else:
                        numeros.insert(3, n)
                        print('Número adicionado na posição 4.')
            
print(numeros)