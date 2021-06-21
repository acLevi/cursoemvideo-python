# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados. 
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = stc = msl = 0

# Pop matriz; First line l - column c

for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um número para a posição [{l+1}, {c+1}]: '))

        # Checking if the number is even
        if n % 2 == 0:
            spar += n

        # Sum of third column values
        if c == 2:
            stc += n 

        # Second line highest value
        if l == 1:
            if n > msl:
                msl = n

        matriz[l][c] = n

# Display matriz

for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]:^5} ]', end='')
    print()

print(f'A soma dos números pares: {spar}')
print(f'Soma dos valoes da terceira coluna: {stc}')
print(f'Maior valor da segunda linha: {msl}')