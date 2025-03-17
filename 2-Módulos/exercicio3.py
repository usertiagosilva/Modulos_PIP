# Escreva uma função que receba uma string e retorne True se todos os caracteres forem alfanuméricos e False caso contrário. Use expressões regulares para resolver este problema.

import re

rule = re.compile(r'[^a-zA-Z0-9]')  # Compilação única

def check_character(string):
    return not bool(rule.search(string))

print(check_character("ABCDEFabcdef123450"))  # True
print(check_character("*&%@#!}{"))  # False
print(check_character("ABCDEFabcdef123450*&%@#!}{"))  # False
