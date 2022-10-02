""" Calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
"""
distancia = float(input('Distância a percorrer em Km: '))
velocidade = float(input('Velocidade média em Km/h: '))
tempo = f'{distancia / velocidade:.2f}'
horas = str(tempo).replace('.', ':')
print('Tempo de viagem:', horas,'h')
