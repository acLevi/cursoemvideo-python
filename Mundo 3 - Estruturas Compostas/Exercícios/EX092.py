# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

cadastro = {}
cadastro['nome'] = str(input('Nome: ')).strip().title()
nasc = int(input('Ano de nascimento: ')) 
cadastro['ano'] = date.today().year - nasc
cadastro['ctps'] = int(input('CTPS: '))
if cadastro['ctps'] > 0:
    cadastro['ano_contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: '))
    cadastro['aposentadoria'] = (cadastro['ano_contratação'] - nasc) + 35

for k, v in cadastro.items():
    print(f'{k}: {v}')
