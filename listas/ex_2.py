""" LISTAS """

# Interação com listas

#2 Exemplo
#  Interação na lista com input com dois laços (while)
notas = []
k = 1

while k <= 4:
    notas.append(float(input('Nota: ')))
    k += 1

soma = k = 0
while k <= 3: # itera na lista notas desde a posição 0 (primeira posição)
    soma += notas[k]
    k += 1

print(f'Média {notas} é {soma/4:.1f}')
