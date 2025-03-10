"""
Sara trabalha no setor de atendimento de uma empresa e precisa verificar rapidamente se os clientes estão
digitando seus números de CPF no formato correto antes de registrar os dados no sistema.
O formato esperado do CPF é: três blocos de 3 dígitos separados por pontos (.), seguidos por um bloco de 2 dígitos separados por um traço (-).
"""

import re

CPF = str(input("Digite o CPF no formato XXX.XXX.XXX-XX: "))

if re.fullmatch(r"\d{3}\.\d{3}\.\d{3}\-\d{2}", CPF):
    print("O CPF está no formato correto.")
else:
    print("O CPF está no formato incorreto.")
