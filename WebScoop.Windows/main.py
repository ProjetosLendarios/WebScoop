import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import os

# Configuração da janela principal
root = tk.Tk()
root.title("WebScoop - Gonçalo Garrido")

# Cores do Python
bg_color = "#306998"  # Azul Python
text_color = "#FFD43B"  # Amarelo Python
button_color = "#FFE873"  # Amarelo claro para botões
button_text_color = "#306998"  # Azul para texto do botão

# Configuração de tamanho e centralização da janela
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg=bg_color)

# Desativar a capacidade de redimensionar a janela
root.resizable(False, False)

# Definir ícone da aplicação
icon_path = os.path.join(os.path.dirname(__file__), "../Docs/icon.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)
else:
    messagebox.showwarning("Aviso", "Ícone não encontrado. O programa continuará sem o ícone.")

# Função para recolher dados de um site
def scrape_data():
    url = "https://www.python.org/blogs/"
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('h2')
        if headlines:
            data = "\n".join([headline.get_text().strip() for headline in headlines])
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, data)
            messagebox.showinfo("Sucesso", "Dados recolhidos com sucesso!")
        else:
            messagebox.showinfo("Informação", "Nenhum dado relevante encontrado.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro", f"Falha ao aceder ao site. Detalhes: {e}")

# Interface gráfica
label = tk.Label(root, text="Clique no botão para recolher dados da web:", bg=bg_color, fg=text_color, font=("Helvetica", 12))
label.pack(pady=10)

scrape_button = tk.Button(root, text="Recolher Dados", command=scrape_data, bg=button_color, fg=button_text_color, font=("Helvetica", 10, "bold"))
scrape_button.pack(pady=10)

result_text = tk.Text(root, wrap='word', height=15, bg="#FFF", fg=bg_color, font=("Consolas", 10))
result_text.pack(pady=10)

# Iniciar a aplicação
root.mainloop()
