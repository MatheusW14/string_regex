"""
Você trabalha em uma biblioteca e está organizando os títulos de livros no sistema.
Você precisa identificar todos os títulos que possuem palavras iniciadas por uma determinada letra,
para criar coleções temáticas baseadas em letras específicas.
Por exemplo, você poderia usar isso para agrupar livros com palavras que começam com a mesma letra,
ajudando na organização ou em campanhas como “Livros com A para você!”.
"""

import re

titulo_livro = str(input("Digite o título dos livro: ")).lower()
letra = str(input("Digite a letra inicial para pesquisa: ")).lower()

padrao = rf"\b{letra}\w*"
palavras = re.findall(padrao, titulo_livro)

print(f"{palavras}")
