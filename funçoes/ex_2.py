""" FUNÇÕES

- Defina uma função fatorial

"""

# Forma invertida de calcular o fatoral
def fat(n: int):
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f # return permite manipular o contúdo devolvendo pra quem o chamou

print(fat(5)) # print só mostra na tela

# Calcula o fatorial de 0 a 4
for i in range(5): print(fat(i))

# Calcula o fatorial de 1 a 5
for i in range(1, 6): print(fat(i))
