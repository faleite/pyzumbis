""" 5. Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem
uma das letras “python” e que tenham mais de 4 caracteres. Não se esqueça de
transformar maiúsculas para minúsculas e de remover
antes os caracteres especiais. """

from string import punctuation


texto = """
The Python Software Foundation and the global Python community welcome
and encourage participation by everyone. Our community is based on mutual
respect, tolerance, and encouragement, and we are working to help each
other live up to these principles. We want our community to be more diverse:
whoever you are, and whatever your background, we welcome you.
""".lower()

# Tratamento da string -> remove caracteres especiais (pontuações)
for carac_esp in punctuation:  # punctuation -> funçaoi do método string
    texto = texto.replace(carac_esp, ' ')

# Funçao que verifica se palavra possui alguma letra dentro da palavra 'python'
def pytonica(palavra):
    for letra in palavra:
        if letra in 'python':
            return True
    return False


resp = []
# Adiciona na lista as palavra que contém alguma letra de 'python'
for palavra in texto.split():
    if pytonica(palavra) and len(palavra) > 4:
        resp.append(palavra)

print(resp)
print(len(resp))

# Com list Comprehension
resp2 = [palavra for palavra in texto.split()
        if pytonica(palavra) and len(palavra) > 4]

print (resp2)
print (len(resp2))
