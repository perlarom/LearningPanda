import pandas as pd

nba_players = pd.read_csv("D:/8vo Cuatri/Almeida/nba_players_a.csv", sep=',', usecols=['Name']).squeeze()

print(type(nba_players))

# Función describe
print(f'Funnción describe cpon una serie: {nba_players.describe()}')

# Función head
print(f'Primeros 5 elementos de una serie:\n {nba_players.head()}')
print(f'\n\nPrimeros 105 elementos de una serie:\n {nba_players.head(10)}')

# Función tail
print(f'\n\n\nÚltimos 5 elementos de una serie:\n {nba_players.tail()}')
print(f'\n\nÚltimos 105 elementos de una serie:\n {nba_players.tail(10)}')