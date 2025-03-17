import hashlib

# 1 - Verificar os algorítimos disponiveis:
print(hashlib.algorithms_available)

# 2 - Algoritimos disponiveis de acordo com o Sistema Operacional:
print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o sha256:
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "A melhor linguagem de programação é Python". encode()
algorithm.update(message)
print(algorithm.hexdigest())

# 4 - Utilizando o MD5:
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())