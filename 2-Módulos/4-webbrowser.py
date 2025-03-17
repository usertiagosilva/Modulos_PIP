# Para manipular o navegador web, podemos usar o módulo webbrowser.
# Com ele, podemos abrir uma URL no navegador padrão do sistema operacional.

import webbrowser

done = False

while not done:
    print("O que voce deseja fazer?")
    print("1. Aprender Python")
    print("2. Aprender sobre módulos")
    print("3. Aprende Python, Fullstack JS, Inglês e No Code")
    print("4. Sair")
    
    choice = input("Digite o número da opção desejada: ")
    
    if choice == "1":
        webbrowser.open("https://www.python.org/")
    elif choice == "2":
        webbrowser.open("https://docs.python.org/3/library/")
    elif choice == "3":
        webbrowser.open("https://onebitcode.com/")
    elif choice == "4":
        done = True
    else:
        print("Opção inválida. Escolha uma opção entre 1 e 4.")
        