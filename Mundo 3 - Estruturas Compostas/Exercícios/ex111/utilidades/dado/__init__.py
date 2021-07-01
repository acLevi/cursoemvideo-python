def leiaDinheiro(prompt):
    valido = False
    while not valido:
        msg = str(input(prompt)).replace(',', '.').strip()
        if msg.isalpha() or msg == '':
            print(f'ERRO! "{msg}" não é um número.')
        else:
            valido = True
            return float(msg)