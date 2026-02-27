#interface gráfica no pyhton
#Tkinter - vem com a instalação do interpretador do python
import tkinter as tk

CORFUNDO = "#D14071"
CORTEXTO ="#FFFFFF"

# 1 - criar a variavel que representa a janela
root = tk.Tk()
root.configure(bg=CORFUNDO) #mudar a cor de fundo da janela
root.title('1- Esqueleto da GUI') #mudar o titulo
root.geometry('600x400') #configurar a largyra e altura
#room.state('zoomed') #inicia a janela maximizada

# Para criar os elementos (widgets) há sempre 2 passos
# 1- Criar a variavel que representa o widget
# tk.Widget (qual janela?, qual texto?)
nome_label = tk.Label(root, text='Digite o seu nome:', bg=CORFUNDO, fg=CORTEXTO, font=("Arial", 14, 'bold'))
# 2- Posicionar o widget na janela
nome_label.pack(pady=20)

nome_entry = tk.Entry(root, width = 30)
nome_entry.pack()

password_label = tk.Label(root, text='Digite a sua password:', bg=CORFUNDO, fg=CORTEXTO, font=("Arial", 14, 'bold'))
password_label.pack(pady=20)

password_entry = tk.Entry(root, width = 30)
password_entry.pack()


# Botão
registar_button = tk.Button(root, text='Registar')
registar_button.pack(pady=(25, 0))


# por último: iniciar o ciclo de eventos, ou seja, abrir a janela
root.mainloop()