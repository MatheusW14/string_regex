"""
João é atendente em uma farmácia e precisa verificar se um cliente forneceu um número de receita válido em uma descrição.
O número da receita é sempre o único número presente no texto fornecido pelo cliente.
Ele quer um programa que extraia esse número diretamente e confirme se o texto está correto, sem a necessidade de trabalhar com listas ou loops.
"""

import re

descricao_receita = str(input("Digite a descricao da receita: "))

num_receita = re.search(r"\d+", descricao_receita)

if num_receita:
    print(f"O número da receita é: {num_receita.group()}")
else:
    print("Nenhum número encontrado na descrição da receita.")
