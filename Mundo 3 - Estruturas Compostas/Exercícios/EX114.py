# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

from urllib import request, error

def urlcheck(link):
    try:
        request.urlopen(link)
    except error.URLError:
        print(f'O site "{link} está indisponível."')
    else:
        print(f'O site {link} está DISPONÍVEL.')


site = 'http://pudim.com.br/'
urlcheck(site)
