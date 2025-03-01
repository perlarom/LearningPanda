import pandas as pd

nba_players = pd.read_csv("D:/8vo Cuatri/Almeida/nba_players_a.csv", sep=',', usecols=['DRtg']).squeeze()
some_value = nba_players.iloc[:5]

addition_1 = some_value + 10
addition_2 = some_value.add(10)

print('Realización de una suma')

print(some_value)
print(addition_1)
print(addition_2)

print('Realización de una resta')
subtract_1 = some_value - 10
subtract_2 = some_value.sub(10)

print(subtract_1)
print(subtract_2)

print('Realización de una división')
division_1 = some_value / 2
division_2 = some_value.div(2)

print(division_1)
print(division_2)

print('Realización de una multiplicación')
multiplication_1 = some_value * 2
multiplication_2 = some_value.mul(2)

print(multiplication_1)
print(multiplication_2)