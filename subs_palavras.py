"""
Nathalia é uma escritora que está revisando um texto para publicação.
Durante o processo, ela percebeu que usou a palavra "bom" repetidamente, quando queria expressar algo mais forte, como "ótimo".
Para economizar tempo, Nathalia quer substituir automaticamente todas as ocorrências da palavra "bom" por "ótimo" no texto.
"""

texto = str(input("Digite o texto a ser revisado: "))

palavra_antiga = input("Qual palavra deseja substituir? ")
palavra_nova = input("Qual a nova palavra? ")

texto_novo = texto.replace(palavra_antiga, palavra_nova)

print(f"{texto_novo}")


# Outra forma de realizar seria:
# import re

# texto = input("Digite o texto a ser revisado: ")
# palavra_antiga = input("Qual palavra deseja substituir? ")
# palavra_nova = input("Qual a nova palavra? ")

# nova_frase = re.sub(rf'\b{palavra_antiga}\b', palavra_nova, texto)
# print(nova_frase)
