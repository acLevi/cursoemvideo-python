numeros = []

# Loop
for c in range(0, 5):
    n = int(input('Digite um número: '))
# Caso o número seja o primeiro a ser digitado ou maior do que o último ele será adicionado ao fim da lista.
    if c == 0 or n >= numeros[-1]:
        numeros.append(n)
        print('Número adicionado ao fim da lista.')
# Se não, o programa irá percorrer os números da lista e verificar se n é menor do que n na posição pos.
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Número adicionado na posição {pos}.')
                break
            pos += 1

print(numeros)