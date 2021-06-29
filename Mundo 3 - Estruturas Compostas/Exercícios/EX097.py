# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    carac = len(msg) + 2
    print('-'*(carac))
    print(f' {msg}')
    print('-'*(carac))


#main
while True:
    frase = str(input('Digite uma frase: '))
    escreva(frase)
    if frase == 'stop':
        break