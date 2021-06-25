# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []
totgols = 0

jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
q = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, q):
    gol = int(input(f'Quantos gols na {c+1}ª partida? '))
    totgols += gol
    gols.append(gol)
    jogador['gols'] = gols
    jogador['total'] = totgols
print('-='*15)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('-='*15)
print(f'O jogador {jogador["nome"]} jogou {q} partidas.')
for i, g in enumerate(gols):
    print(f'    -> Na {i+1}ª partida, fez {g} gols.')
