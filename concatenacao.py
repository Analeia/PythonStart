"""
Concatenação e Formatação de Saída

Resumo:
Este script demonstra como exibir dados no terminal juntando textos fixos (rótulos)
com o tipo retornado pela função type(), utilizando múltiplos argumentos separados
por vírgula no print().

Dica de estudo:
Além de separar argumentos com vírgula no print(), em Python também é muito comum
concatenar usando f-strings (ex: f"Nome: {name_do_filme}") ou o operador + (entre strings).
"""

# ----------------------------------------------------------------------
# 1. Definição das variáveis do filme
# ----------------------------------------------------------------------
name_do_filme = "Top Gun Maverick"  # String
ano_de_lancamento = 2022  # Inteiro
nota_do_filme = 8.5  # Float
plan_inclued = False  # Booleano
atores_principais = ["Tom Cruise", "Miles Teller", "Jennifer Connelly"]  # Lista

# ----------------------------------------------------------------------
# 2. Exibição combinando texto descritivo e o tipo das variáveis
# ----------------------------------------------------------------------
print("Nome do filme:", type(name_do_filme))
print("Ano de lançamento:", type(ano_de_lancamento))
print("Nota do filme:", type(nota_do_filme))
print("Plano incluído:", type(plan_inclued))
print("Atores principais:", type(atores_principais))
