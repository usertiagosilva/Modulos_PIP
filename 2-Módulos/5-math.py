import math

# 1 - Acessar o numero PI:
print(math.pi)
print(f"{math.pi:.2f}")

# 2 - Acessar o numero de Euler:
print(math.e)
print(f"{math.e:.2f}")

# 3 - Arredondando numeros para cima e para baixo:
num1 = 10.6
print(math.ceil(num1))
print(math.floor(num1))

# 4 - Fatorial de um numero:
num2 = int(input("Digite um numero para saber o fatorial:\n"))
print(math.factorial(num2))

# 5 - Potência de numeros:
print(math.pow(2, 3))

# 6 - Raiz quadrada de um numero:
print(math.sqrt(9))

# 7 - MDC de dois numeros:
mdc = math.gcd(10, 5)
print(mdc)

# 8 - Logaritimo de um numero:
print(math.log(100))
