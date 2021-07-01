# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import date
    y = date.today().year
    idade = y - ano
    print(f'Com {idade} anos:', end=' ')
    if idade < 16:
        return 'NÃO VOTA.'
    elif 16 <= idade <= 18 or idade > 65:
        return 'VOTO OPCIONAL.'
    else:
        return 'VOTO OBRIGATÓRIO.'


data = int(input('Ano de nascimento: '))
print(voto(data)) 