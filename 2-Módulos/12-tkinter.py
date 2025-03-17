# O tkinter é uma biblioteca padrão do Python para criar interfaces gráficas.
import tkinter as tk

# 1- Criando a janela :
window = tk.Tk()
window.geometry("400x200")
window.title("Gerenciador de frases")

# 2 - Adicionando o Frame (para organizar os widgets) :
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# 3 - Adicionando o Label (para exibir texto) :
label = tk.Label(frame, text="Helow World!")
label.pack(fill='x', expand=True)

# 4 - Adicionando o input (para receber texto) :
frase_lab = tk.Label(frame, text="Digite uma frase:")
frase_lab.pack(fill='x', expand=True)
# Entrada de texto
frase_input = tk.Entry(frame)
frase_input.pack(fill='x', expand=True)

# 5 - Função para alterar o texto da label :
def alterar_texto():
    label.config(text=frase_input.get())
    
# 6 - Adicionando o botão (para executar a ação) :
button = tk.Button(frame, text="Enviar", command=alterar_texto)
button.pack()

window.mainloop()
