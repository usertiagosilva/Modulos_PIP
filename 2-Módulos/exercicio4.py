# Exercicio 4: Jogo de adivinhação de número entre 1 e 10.
import random

def menu():
    print("\n🎯 Adivinhe o Número:\n")
    print("1 - Iniciar")
    print("2 - Sair")

while True:
    menu()
    
    try:
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 2:
            print("Fim do Jogo. Obrigado por jogar!")
            break
        if opcao == 1:
            numero = random.randint(1, 10)
            
            try:
                tentativa = int(input("Digite um número entre 1 e 10: "))
                
                if tentativa < 1 or tentativa > 10:
                    print("Por favor, digite um número entre 1 e 10!")
                elif tentativa == numero:
                    print("\n🎉 Parabéns! Você acertou!")
                else:
                    print(f"\n❌Que pena! O número sorteado foi {numero}.")
            except ValueError:
                print("Erro: Digite um número válido!")
        
        else:
            print("\n❌Opção inválida! Escolha 1 para jogar ou 2 para sair.")
    
    except ValueError:
        print("Erro: Digite um número válido!")
