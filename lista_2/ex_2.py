""" Determine se um ano é bissexto. Verifique no Google como fazer isso... """

from calendar import isleap

ano = int(input('Ano: '))

if isleap(ano) == True:
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} não é um ano bissexto')

# Resolução sem a lib isleap(year)
#  if ano % 4 != 0:
    #  print('Não é um ano bissexto')
#  else:
    #  if ano % 100 != 0:
        #  print('É um ano bissexto')
    #  else:
        #  if ano % 400 != 0:
            #  print('Não é um ano bissexto')
        #  else:
            #  print('É um ano bissexto')


