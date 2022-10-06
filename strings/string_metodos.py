""" Métodos do objeto strings

- String também é um método em python

"""

# Obter todos os métodos de uma string:
dir('abacate')
# Os métodos com __ são reservados, não usamos* (ex.: __add__)
# Os métodos que podemos usar estão entre aspas (ex.: 'upper')
# Podemos descobrir a função de cada método com o help('upper')
# O help() nos passa a sintaxe e a descrição: help('abacate'.upper)
# Ex.:
print('abacate'.upper()) # 'ABACATE'

# Método find
s = 'um tigre, dois tigres, três tigres'
print(s.find('tigre')) # mostra em que posição esta a string 'tigre'
# >>> 3
print(s.find('tigre', 4)) # posição que esta a string 'tigre', buscando a partir da 4 posição
# >>> 15
print(s.find('tigre', 16)) # posição que esta a string 'tigre', buscando a partir da 16 posição
# >>> 28

# Método replace
print(s.replace('tigre', 'gato')) # faz a troca da string 'tigre' para 'gato'
# >>> um gato, dois gatos, três gatos
print(s) # veja que o replace não altera a variavel s
# >>> 'um tigre, dois tigres, três tigres'
s = s.replace('tigre', 'gato') # para alterar a variavel é preciso refatorar
print(s)
# >>> 'um gato, dois gatos, três gatos'


