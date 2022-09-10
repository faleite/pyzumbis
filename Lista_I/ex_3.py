""" Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
Calcule o total em segundos.
"""

dias = int(input('Informe a quatidade de dias: '))
horas = int(input('Informe a quatidade de horas: '))
minutos = int(input('Informe a quatidade de minutos: '))
segundos = int(input('Informe a quatidade de segundos: '))

# Resolução do professor:
total_1 = dias*24*60*60 + horas*60*60 + minutos*60 + segundos
print(total_1)

# Minha resolução
dias = (dias * 24 * 60) * 60
horas = (horas * 60) * 60
minutos = minutos * 60

total = dias + horas + minutos + segundos
print(f'O valor total em segundos é: {total}')
