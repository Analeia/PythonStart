"""
Tipos de Dados em Python

Resumo:
Este script apresenta os tipos de dados fundamentais da linguagem Python
(string, int, float, bool e list) utilizando informações de um filme como exemplo.

Conceitos principais:
- Tipagem Dinâmica: o Python infere o tipo do dado automaticamente.
- Padrão snake_case: convenção recomendada (PEP 8) para nomes de variáveis.
- Função type(): retorna a classe/tipo de uma variável.
"""

# ----------------------------------------------------------------------
# 1. Definição das variáveis com diferentes tipos de dados
# ----------------------------------------------------------------------
name_do_filme = "Top Gun Maverick"  # String (str): texto
ano_de_lancamento = 2022  # Inteiro (int): números inteiros
nota_do_filme = 8.5  # Float (float): números decimais
plan_inclued = False  # Booleano (bool): True ou False
atores_principais = ["Tom Cruise", "Miles Teller", "Jennifer Connelly"]  # Lista (list): coleção ordenada

# ----------------------------------------------------------------------
# 2. Verificação e exibição dos tipos de cada variável
# ----------------------------------------------------------------------
print(type(name_do_filme))
print(type(ano_de_lancamento))
print(type(nota_do_filme))
print(type(plan_inclued))
print(type(atores_principais))
