# Exemplos de utilização de coleções em Python
from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1- Contar itens de uma lista:
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(fruits)
print(Counter(fruits))

# 2 - Utilizando tupla nomeada (namedtuple)::
music = namedtuple('music', ['name', 'genre', 'year'])
m1 = music("please me", "pop", 2019)
m2 = music("bad guy", "pop", 2019)
print(m1)
print(m2)

# 3 - Ordenando dicionários:
studants = {"Rodrigo": 25, "Maria": 22, "João": 30, "Ana": 27}
a = sorted(studants.items(), key=itemgetter(0))
print(studants)
print(a)

# 4 - Utilizando fila ambas extremidades:
d = deque([20, 30, 40, 50, 60])
d.appendleft(10)
print(d)
d.append(70)
print(d)
d.popleft()
print(d)
d.pop()
print(d)
