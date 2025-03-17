# Inverter uma string de trás pra frente
def inverse(s):
    return s[::-1]

# letras com índice par
def even_chars(s):
    return s[::2]

# letras com índice ímpar
def odd_chars(s):
    return s[1::2]

# quantidade de vogais
def vowels(s):
    return sum([1 for c in s if c in 'aeiouAEIOU'])

# quantidade de consoantes
def consonants(s):
    return sum([1 for c in s if c not in 'aeiouAEIOU'])