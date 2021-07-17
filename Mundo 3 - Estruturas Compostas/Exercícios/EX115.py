from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

dado = 'Mundo 3 - Estruturas Compostas\Exercícios\ex115\dados.txt'
abrir(dado)

while True:
    reposta = menu(['Ver pessoas cadastradas', 'Cadastrar uma pessoa', 'Sair do sistema'])
    if reposta == 1:
        ler(dado)
    elif reposta == 2:
        title('CADASTRO', '+')
        nome = input('Nome: ').strip().title()
        idade = leiaInt('Idade: ')
        cadastrar(dado, nome, idade)
    elif reposta == 3:
        title('Até logo!', '-')
        break
    else:
        print('Opção inválida.')
        sleep(2)