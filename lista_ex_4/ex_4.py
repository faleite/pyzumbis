""" 4. Seja o statement sobre diversidade: “The Python Software Foundation
and the global Python community welcome and encourage participation
by everyone. Our community is based on mutual respect, tolerance,
and encouragement, and we are working to help each other live up to these
principles. We want our community to be more diverse: whoever you are,
and whatever your background, we welcome you.”.
Gere uma lista de palavras deste texto com split(), a seguir crie uma lista com
as palavras que começam ou terminam com uma das letras “python”.
Imprima a lista resultante.
Não se esqueça de remover antes os caracteres especiais
e cuidado com maiúsculas e minúsculas. """

from string import punctuation


texto = """
The Python Software Foundation and the global Python community welcome
and encourage participation by everyone. Our community is based on mutual
respect, tolerance, and encouragement, and we are working to help each
other live up to these principles. We want our community to be more diverse:
whoever you are, and whatever your background, we welcome you.
""".lower()

for caract_esp in punctuation:
    texto = texto.replace(caract_esp, ' ')

lista_palavras = []

for palavra in texto.split():
    if palavra[0] in 'python' or palavra[-1] in 'python':
        lista_palavras.append(palavra)

# Com list comprehension
resp = []

resp = [p for p in texto.split()
        if p[0] in 'python' or p[-1] in 'python']

print(resp)
print()
print(lista_palavras)
