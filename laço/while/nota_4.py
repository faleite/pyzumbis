""" REPETIÇÃO COM O 'WHILE'
- contadores incremento constante
- acumuladores variável
- Comando "break" sai de qualquer repetição
"""

# Se não soubesse quando terminar uma repetição?
# Ex. quero somar até a pessoa digitar um zero:
# Para isso usamos o comando chamado "break"

soma = 0
n = 0
while True: # Loop infinito, condição de parada -> não para nunca
    x = int(input('n (zero sai): '))
    if x == 0:
        break
    else:
        n = n + 1
        soma = soma + x

print(f'Soma: {soma}')
print(f'Média: {soma / n}')

# Código apenas soma sem a média
#  while True: # Loop infinito, condição de parada -> não para nunca
    #  x = int(input('n (zero sai): '))
    #  if x == 0:
        #  break
        #  soma = soma + x








