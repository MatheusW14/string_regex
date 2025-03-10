"""
Carlos precisa de um programa que leia as informações, capture cada parte separadamente, nome, o sobrenome e o ano de nascimento para preencher os campos do sistema.
Ajude Carlos criando um programa que solicite o nome completo e o ano de nascimento de um paciente e exiba-os separadamente.
"""

import re

nome = input("Digite o nome completo do paciente(PrimeiroNome Sobrenome - Ano): ")

primeiro_nome = re.search(r"\b[A-Z][a-z]*", nome)
sobrenome = re.search(r"\b[A-Z][a-z]*", nome.split()[1])
idade = re.search(r"\d{4}", nome)

if primeiro_nome:
    print(f"Primeiro nome: {primeiro_nome.group()}")
if sobrenome:
    print(f"Sobrenome: {sobrenome.group()}")
if idade:
    print(f"Ano de nascimento: {idade.group()}")
else:
    print("Informações não encontradas.")


# import re

# dados = input("Digite o nome completo e o ano de nascimento do paciente: ")
# padrao = r'(\w+) (\w+) - (\d{4})'

# resultado = re.search(padrao, dados)

# if resultado:
# primeiro_nome = resultado.group(1)
# sobrenome = resultado.group(2)
# ano_nascimento = resultado.group(3)

# print(f"Primeiro Nome: {primeiro_nome}")
# print(f"Sobrenome: {sobrenome}")
# print(f"Ano de Nascimento: {ano_nascimento}")
# else:
# print("Formato inválido!")
