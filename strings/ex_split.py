""" Transformar uma variavel

*Uso do método: split

[Input]: 23/10/1984
[Out]: 23 de outubro de 1984

"""

# O método split() sem parametro separa string por espaço, tab e quebra de linha
mes = '''janeiro fevereiro março abril maio junho
         julho agosto setembro outubro novembro dezembro'''.split()

# Desta forma: split('/') usa o caractere / como separador e atribui a cada variavel
d,m,a = input('dd/mm/aaaa: ').split('/')

print(f'{d} de {mes[int(m)-1]} de {a}')

#1 Minha resolução
#  data = input('Digite uma data (DD/MM/AAAA): ')

#  sep = data.split('/')

#  meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
         #  'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
         #  ]

#  mes = int(sep[1]) - 1

#  print(f'{sep[0]} de {meses[mes]} de {sep[2]}')
