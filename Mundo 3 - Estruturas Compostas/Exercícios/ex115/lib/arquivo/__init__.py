from ex115.lib.interface import *

def abrir(path):
    try:
        dados = open(path, mode='rt')
        dados.close()
    except FileNotFoundError:
        dados = open(path, mode='wt+')
        dados.close()  

def ler(path):
    try:
        dados = open(path, mode='rt')
    except FileNotFoundError:
        print('Erro ao ler o arquivo.')
    else:
        title('PESSOAS CADASTRADAS', '=')
        for l in dados:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        dados.close()
           

def cadastrar(path, nome='Desconhecido', idade=0):
    try:
        dados = open(path, mode='at')
    except FileNotFoundError:
        print('Erro ao ler o arquivo.')
    else:
        dados.write(f'{nome};{idade}\n')
        print(f'{nome} registrado com sucesso.')
    finally:
        dados.close()
