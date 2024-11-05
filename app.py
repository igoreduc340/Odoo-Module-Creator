import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
from dotenv import load_dotenv  # type: ignore

load_dotenv()

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

# Caminhos de arquivos
standard_module_path = os.getenv('CAMINHO_STANDARD_MODULE')


# Função para criar campos de entrada
def create_input_label(frame, text):
    label = tk.Label(frame, text=text, font=FONT_LABEL, bg=FRAME_BG_COLOR, fg=LABEL_FG_COLOR)
    label.pack(pady=(10, 5))
    entry = tk.Entry(frame, font=FONT_ENTRY, bd=1, relief="flat", bg=ENTRY_BG_COLOR)
    entry.pack(pady=(0, 10))
    return entry

def handle_module_button_click():
    module_name = module_name_entry.get()
    file_name = file_name_entry.get()
    selected_option = module_option_combobox.get()
    
    if not module_name or not file_name:
        messagebox.showerror("Aviso", "Você precisa preencher os dois campos.")
        return
    
    try:
        res = subprocess.run(['python3', standard_module_path, module_name, file_name, selected_option],
                             check=True, text=True, capture_output=True)
        if res.returncode == 0:
            root.destroy()
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro na execução do script", f"Erro: {e.stderr}")


# Efeito de hover no botão
def on_hover_enter(event):
    button.config(bg=BUTTON_HOVER_BG_COLOR)

def on_hover_leave(event):
    button.config(bg=BUTTON_BG_COLOR)

# Criação da janela principal
root = tk.Tk()
root.title("Odoo Gerenciador")
root.geometry("400x400")
root.configure(bg=BG_COLOR)

# Criando o notebook
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Primeira aba para Módulo
module_frame = tk.Frame(notebook, padx=20, pady=20, bg=FRAME_BG_COLOR)
notebook.add(module_frame, text="Modulo")

# Componentes para a primeira aba
module_label = tk.Label(module_frame, text="Selecione uma opção:", font=FONT_LABEL, bg=FRAME_BG_COLOR, fg=LABEL_FG_COLOR)
module_label.pack(pady=(0, 10))

module_options = ["Sylvia Design", "Nave", "Asisto Base"]
module_option_combobox = ttk.Combobox(module_frame, values=module_options, state="readonly", font=FONT_LABEL)
module_option_combobox.set(module_options[0])
module_option_combobox.pack(pady=(0, 15))

module_name_entry = create_input_label(module_frame, "Nome do Módulo:")
file_name_entry = create_input_label(module_frame, "Nome do Arquivo:")

# Botão de ação para a primeira aba
button = tk.Button(module_frame, text="Clique aqui", command=handle_module_button_click,
                   font=FONT_LABEL, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR, bd=0, relief="flat")
button.pack(pady=(15, 0))

button.bind("<Enter>", on_hover_enter)
button.bind("<Leave>", on_hover_leave)

# Componentes para a segunda aba


# Foco no primeiro campo de entrada
module_name_entry.focus_set()

# Iniciar o loop principal
root.mainloop()
