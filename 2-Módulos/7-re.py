import re

text = "OneBitCode: Transformamos pessoas em programadores sem limites!"

# 1 - Índice inicial e final de palavras.

# O r significa que estamos trabalhando com uma string bruta (raw string)
match = re.search(r'pessoas em programadores', text)
print('Indice inicial', match.start())
print('Indice final', match.end())

# 2 - Buscando o índice que possui o ponto
site = "www.onebitcode.com"
match = re.search(r'\.', site)
print(match)

# 3 - Buscando uma lista de caracteres dentro de uma frase:
pattern = "[a-m]"
result = re.findall(pattern, text)
print(text)
print(result)

# 4 - Verificando o inicio de uma string
rule = r'^A'
phrases = ['A casa está suja', ' porta está aberta', 'A janela está fechada'] 
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não corresponde: {f}")
    
    
# 5 - Verificando o final de uma string
rule_end = r'!$'
phrases2 = ['A casa está suja!', ' porta está aberta', 'A janela está fechada']
for f in phrases2:
    if re.search(rule_end, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não corresponde: {f}")
