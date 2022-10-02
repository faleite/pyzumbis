""" Escreva um programa para calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
Considere que um fumante perde 10 minutos de vida a cada cigarro,
calcule quantos dias de vida um fumante perderá. Exiba o total de dias. """

n_cigarros = int(input('Quantos cigarros por dia: '))
anos_fumou = int(input('Quantos anos fumou: '))

tempo = (n_cigarros * 10) * (anos_fumou * 365) / 1440

print('Total de dias perdidos: {:.1f}'.format(tempo))
