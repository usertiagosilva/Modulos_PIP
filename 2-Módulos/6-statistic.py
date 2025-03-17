import statistics

# 1 - Aplicar a média:
print(statistics.mean([3, 2, 5, 8, 9]))

# 2 - Aplicar a mediana:
print(statistics.median([3, 2, 5, 8, 9]))

# 3 - Aplicar a moda (numero que mais se repete):
print(statistics.mode([3, 2, 5, 8, 9, 3, 3, 3]))

# 4 - Desvio padrão:
#Quanto mais próximo de 0 for o desvio padrão, significa que os dados do conjunto estão menos dispersos
print(statistics.stdev([3, 2, 5, 8.2, 9, 10, 6, 8.5]))


