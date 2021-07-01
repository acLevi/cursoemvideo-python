# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# Quantidade de notas  
# A maior nota    
# A menor nota 
# A média da turma
# A situação (opcional)

def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas do alunos
    : param sit: valor opcional, indicando se deve ou não adicionar a situação do aluno.
    : return: dicionário com várias informações sobre a situação da turma.
    """

    dic = {}
    dic['total'] = len(dic)
    dic['maior'] = max(dic)
    dic['menor'] = min(dic)
    dic['média'] = sum(dic) / len(dic       )
    if sit:
        if dic['média'] >= 7.0:
            dic['situação'] = 'APROVADO'
        elif dic['média'] >= 5.0:
            dic['situação'] = 'RECUPERAÇÃO'
        else:
            dic['situação'] = 'REPROVADO.'
    return dic


print(notas(5.5, 2.5, 1.5, 10, 10, 10, sit=True))