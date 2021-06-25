
jogadores = []
dados = {}
gols = []

while True:
    dados.clear()
    totgols = 0
    dados['nome'] = str(input('Nome do jogador: ')).strip().title()
    q = int(input(f'Quantos partidas {dados["nome"]} jogou? '))
    for c in range(0, q):
        gols.append(int(input(f'    Quantos gols na {c+1}ª partida? ')))
    dados['gols'] = gols[:]
    gols.clear()
    totgols = sum(dados['gols'])
    dados['total'] = totgols
    jogadores.append(dados.copy())
    while True:
        answer = str(input('Quer continuar? ')).lower().strip()[0]
        if answer in 'sn':
            break
    if answer in 'n':
        break
print('-='*30)
print(f'{"Nº":<3} {"Nome":<15} {"Gols":<15} {"Total":<3}')
print('--'*30)
for j in jogadores:
    print(f'{jogadores.index(j):<3} {j["nome"]:<15} {str(j["gols"]):<15} {j["total"]:<3}')
while True:
    print('--'*30)
    op = int(input('Mostrar dados de qual jogador? '))
    if op == 999:
        break
    if 0 <= op <= len(jogadores) - 1:
        print(' > DADOS DO JOGADOR', jogadores[op]['nome'].upper())
        for i, g in enumerate(jogadores[op]['gols']):
            print(f' No {i+1}º fez {g} gols.')
    else:
        print(f'Não existe jogador com código {op}.')
