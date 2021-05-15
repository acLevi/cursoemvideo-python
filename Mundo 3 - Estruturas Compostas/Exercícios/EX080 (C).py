numeros = []

for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n >= numeros[-1]:
        numeros.append(n)
        print('Número adicionado ao fim da lista.')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Número adicionado na posição {pos}.')
                break
            pos += 1

print(numeros)