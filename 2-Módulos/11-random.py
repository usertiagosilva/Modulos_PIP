# Random é um módulo que gera números aleatórios. Para usá-lo, é necessário importá-lo.
import random

# 1 - Seleciona valor aleatório de uma lista:
list1 = [7, 5, 6, 9, 3, 10, 12]
print(random.choice(list1))

# 2 - Gera um número aleatório em um intervalo de valores
r1 = random.randint(1, 100)
print(r1)

# 3 - Seleciona caractere aleatório de uma string:
name = "Curso de Python da OneBitCode"
r2 = random.choice(name)
print(r2)

# 4 - Sleciona mais de um valor aleatório:
# Sintaxe: random.sample(sequencia, tamanho)
print(random.sample(list1, 2))
print(random.sample(name, 5))
s = "hello world"
print(random.sample(s, 4))
