# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

# Declarando a tupla com os times
times = ('Flamengo', 'Sport', 'Santos', 'Bahia', 'Bragantino', 'Grêmio', 'Palmeiras', 'Athletico-PR', 'Fluminense', 'Fortaleza', 'Internacional', 'Ceará', 'América-MG', 'São Paulo', 'Juventude', 'Cuiabá', 'Corinthians', 'Chapecoense', 'Atlético-GO')

# Mostrando os times
print(f'Lista de times do brasileirão: {times}')
print()
# a) 5 primeiros times
print(f'a) Os 5 primeiros são {times[:5]}')
print()
# b) Os últimos 4 colocados
print(f'b) Os últimos 4 colocados são {times[-4:]}')
print()
# c) Times em ordem alfabética
print(f'c) Times em ordem alfabética: {sorted(times)}')
print()
# d) Posição do time da Chapecoense
times.index('Chapecoense')
print(f'd A Chapecoense está na {times.index("Chapecoense")}ª')
print()