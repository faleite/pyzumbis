""" FUNÇÕES
- len, int, float, print, input e etc... São funções do Python
- Podemos criar as nossas próprias funções
- Utilizamos "def" para definir a função e "return" para devolver algum valor
- Existem funções que não devolvem nada. Por padrão em Python devolve "None"
"""

# 1 Exemplo
# Esta função retorna se o parâmetro x é par
# Essas linhas não serão executadas imediatamente
# É preciso chamar a função para executá-la
def épar(x):
    return x % 2 == 0

# Podemos chamar a função com print
print(épar(13))
print(épar(12))

# Ou atraves do python interativo (python -i ex_1.py)
# >>> épar(13)
# >>> False
# >>> épar(12)
# >>> True
