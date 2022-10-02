""" LISTAS """

# Interação com listas

#1 Exemplo
notas = [6, 7, 8, 9, 10]
soma = 0
k = 0

while k < len(notas): # enquanto contador k for menor que o tamaho de notas
    soma += notas[k] # notas[k], a cada volta no laço acessa uma posição da lista notas
    k += 1 # a cada volta no laço adiciona 1 ao k fazendo interação por todos os elemntos da lista

print('Soma:', soma)
print('Média:', soma/len(notas))
