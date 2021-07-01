# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

def title(msg):
    l = len(msg) + 2
    print('-' * l)
    print(f'{msg} ')
    print('-' * l)


while True:
    ask = str(input('Função ou biblioteca > ')).strip().lower()
    if ask != 'fim':
        print('\033[1;44m')
        title(f'Analisando {ask}()')
        print('\033[1;107m'+'\033[1;30m')
        help(ask)
        print('\033[1;44m')
        title(f'{"Fim da análise"}')
        print('\033[0;0m')
    else:
        break