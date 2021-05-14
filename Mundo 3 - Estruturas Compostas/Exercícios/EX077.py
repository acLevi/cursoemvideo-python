# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
# Tupla
palavras = ('Casa', 'Roupa', 'Escola', 'Caderno', 'Faca', 'Bola', 'Twitter', 'Google', 'Computador', 'Igreja', 'Floresta', 'Deserto', 'Vento', 'Bombeiros', 'Cidade', 'Centro')

# Mostrando as vogais
for p in palavras:
    print(f'Na palavra {p.upper()} temos', end=' ')
    for letras in p:
        if letras.upper() in 'AEIOU':
            print(letras.upper(), end=' ')
    print()
