# Modulo que utiliza o python para acessar informaçãos do sistema operacional
import os

# 1 - Consultar as funcionalidades do módulo os:
# help(os)

# 2 - Retornar a pasta atual:
print(os.getcwd())

# 3 - Listar os arquivos e pastas do diretório atual:
print(os.listdir())

# 4 - Apresentar versão do SO:
os.system('ver')

# 5 - Configurações da maquina:
os.system('systeminfo')

# 6 - Limpar a tela:
os.system('cls')
