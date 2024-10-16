import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

# Definindo constantes de estilo
BG_COLOR = "#f5f5f5"
FRAME_BG_COLOR = "#ffffff"
TITLE_FG_COLOR = "#333333"
LABEL_FG_COLOR = "#444444"
BUTTON_BG_COLOR = "#28a745"
BUTTON_FG_COLOR = "#ffffff"
FOOTER_FG_COLOR = "#888888"
FONT_TITLE = ("Helvetica Neue", 20, "bold")
FONT_LABEL = ("Helvetica Neue", 12)
FONT_ENTRY = ("Helvetica Neue", 12)
ENTRY_BG_COLOR = "#e8e8e8"
BUTTON_HOVER_BG_COLOR = "#218838"

def on_button_click():
    module_name = entry1.get()
    file_name = entry2.get()
    
    if not module_name or not file_name:
        messagebox.showwarning("Aviso", "Você precisa preencher os dois campos.")
        return
    
    caminho_standard_module = '/home/user/Projects/scripts/standard_module.py'
    
    try:
        resultado = subprocess.run(['python3', caminho_standard_module, module_name, file_name],
                                    check=True, text=True, capture_output=True)
        if resultado.returncode == 0:
            root.destroy()
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro na execução do script", f"Erro: {e.stderr}")

# Criação da janela principal
root = tk.Tk()
root.title("Odoo Gerenciador")
root.geometry("400x400")
root.configure(bg=BG_COLOR)

# Frame principal
frame = tk.Frame(root, padx=20, pady=20, bg=FRAME_BG_COLOR, bd=2, relief="flat")
frame.pack(expand=True, fill='both')

# Seleção de opção
label = tk.Label(frame, text="Selecione uma opção:", font=FONT_LABEL, bg=FRAME_BG_COLOR, fg=LABEL_FG_COLOR)
label.pack(pady=(0, 10))

opcoes = ["Sylvia Design", "Navê", "Asisto Base"]

combobox = ttk.Combobox(frame, values=opcoes, state="readonly", font=FONT_LABEL)
combobox.set(opcoes[0])
combobox.pack(pady=(0, 15))

# Função para criar campos de entrada
def create_input_label(frame, text):
    label = tk.Label(frame, text=text, font=FONT_LABEL, bg=FRAME_BG_COLOR, fg=LABEL_FG_COLOR)
    label.pack(pady=(10, 5))
    entry = tk.Entry(frame, font=FONT_ENTRY, bd=1, relief="flat", bg=ENTRY_BG_COLOR)
    entry.pack(pady=(0, 10))
    return entry

entry1 = create_input_label(frame, "Nome do Módulo:")
entry2 = create_input_label(frame, "Nome do Arquivo:")

# Botão de ação
button = tk.Button(frame, text="Clique aqui", command=on_button_click,
                   font=FONT_LABEL, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR, bd=0, relief="flat")
button.pack(pady=(15, 0))

# Efeito hover no botão
def on_enter(event):
    button.config(bg=BUTTON_HOVER_BG_COLOR)

def on_leave(event):
    button.config(bg=BUTTON_BG_COLOR)

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

# Rodapé
footer = tk.Label(frame, text="© 2024 Odoo Gerenciador", font=("Helvetica Neue", 10), bg=FRAME_BG_COLOR, fg=FOOTER_FG_COLOR)
footer.pack(side="bottom", pady=(20, 0))

# Foco no primeiro campo de entrada
entry1.focus_set()

# Inicia o loop principal
root.mainloop()
