"""
Entrada de Dados (input) e Conversão de Tipos (Type Casting)

Resumo:
Este script demonstra como interagir com o usuário via terminal usando input(),
e como converter os dados recebidos (que sempre chegam como string) para outros
tipos numéricos usando int() e float().

Conceitos principais:
- input(): aguarda e lê a digitação do usuário sempre no formato texto (str).
- int(): converte a string em número inteiro.
- float(): converte a string em número de ponto flutuante (decimal).
"""

# ----------------------------------------------------------------------
# 1. Variáveis base de exemplo (dados do filme)
# ----------------------------------------------------------------------
name_do_filme = "Top Gun Maverick"  # String
ano_de_lancamento = 2022  # Inteiro
nota_do_filme = 8.5  # Float
plan_inclued = False  # Booleano
atores_principais = ["Tom Cruise", "Miles Teller", "Jennifer Connelly"]  # Lista

# ----------------------------------------------------------------------
# 2. Entrada de dados do usuário e conversão de tipos
# ----------------------------------------------------------------------
nome_do_usuario = input("Digite seu nome: \n")
ano_de_nascimento = int(input("Digite o ano de nascimento: \n"))
nota_do_usuario = float(input("Digite a nota do filme: \n"))
