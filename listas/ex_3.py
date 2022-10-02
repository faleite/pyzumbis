""" LISTAS """

# Interação com listas

#3 Exemplo
notas = []
k = 0
soma = 0
while k <= 3:
    notas.append(float(input('Nota: ')))
    soma += notas[k]
    k += 1

print(f'Média {notas} é {soma/4:.1f}')
