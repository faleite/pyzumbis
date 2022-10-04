""" Concatenação
- Faça um programa que leia uma palavra e troque as vogais por "*"
"""

palavra = input('Palavra: ')
k = 0 # Contador para pegar a primeira posição em diante
troca = '' # Acomulador de concatenação de caracteres

while k < len(palavra): # Enquanto k não chegar no ultimo caractere da palavra
    if palavra[k] in 'aeiou': # Pergunto se a posição atual é uma vogal
        troca += '*' # Se for vogal troca por asterisco e concatene na variavel
    else: # se não faça:
        troca += palavra[k] # Concatene o caractere na variavel
    k += 1 # va para a proxima posição

print(troca)


