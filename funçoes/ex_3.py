""" FUNÇÕES

- Variáveis locais e globais

"""

#1 Exemplo
# A Fatec fica dentro de um parque Tecnológico

# jose global == variavel global
jose = 'entrou 6h' # Vigia do parque Tecnológico, que engloba a Fatec

def fatec():
    global jose # Usado para transformar a variavel em global
    # jose local == variavel local, vale só dentro da def fatec()
    jose = 'entrou 8h' # Vigia da Fatec
    print(jose)

print(jose) # global
fatec() # local
print(jose) # global
