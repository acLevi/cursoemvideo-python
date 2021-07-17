def line(size=42, style='-'):
    print(style * size)

def title(msg, l='-'):
    line(style=l)
    print(msg.center(42))
    line(style=l)

def leiaInt(promt):
    while True:
        try:
            n = int(input(promt))
        except (ValueError, NameError):
            print('Opção inválida.')
            continue
        else:
            return n

def menu(list):
    title('MENU')
    c = 1
    for i in list:
        print(f'{c} - {i}')
        c += 1
    line()
    opc = leiaInt('Sua opção: ')
    return opc