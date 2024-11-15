import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import os

# Configuração da janela principal
root = tk.Tk()
root.title("WebScoop - Gonçalo Garrido")
root.geometry("600x400")

# Centralizar a janela na tela
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

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
label = tk.Label(root, text="Clique no botão para recolher dados da web:")
label.pack(pady=10)

scrape_button = tk.Button(root, text="Recolher Dados", command=scrape_data)
scrape_button.pack(pady=10)

result_text = tk.Text(root, wrap='word', height=15)
result_text.pack(pady=10)

# Iniciar a aplicação
root.mainloop()
