import tkinter as tk
from tkinter import ttk, messagebox
import os

# ============================================
# LISTA DE COMPRAS - Aplicativo em Tkinter
#=============================================

ARQUIVO = "lista_compras.txt"

class ListaComprasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🛒 Lista de Compras")
        self.root.geometry("750x550")
        self.root.configure(bg="#f0f4f8")
        
        # Dados em memória
        self.itens = []
        self.item_selecionado = None
        
        self.criar_widgets()
        self.carregar_do_arquivo()
        self.atualizar_lista()
    
    def criar_widgets(self):
        # ========== TÍTULO ==========
        lbl_titulo = tk.label(
            self.root,
            text="🛒 LISTA DE COMPRAS",
            font=("Arial", 20, "bold"),
            bg="#f0f4f8",
            fg="#1a5276"
        )
        lbl_titulo.pack(pady=10)
        
        # =========== FRAME DE ENTRADA ============
        frame_entrada = tk.Frame(self.root, bg="#f0f4f8")
        frame_entrada.pack(pady=10, padx=20, fill="x")
        
        # Descrição
        tk.Label(frame_entrada, text="Descrição: ", font=("Arial, 11"), bg="#f0f4f8", fg="#2c3e50").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.txt_descrição = tk.Entry(frame_entrada, font=("Arial",11), widht=30, relief="solid", bd=1)
        self.txt_descrição.grid(row=0, column=1, padx=5, pady=5)
        
        # Quantidade
        tk.Label(frame_entrada, text="Quantidade: ", font=("Arial, 11"), bg="#f0f4f8", fg="#2c3e50").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.txt_quantidade = tk.Entry(frame_entrada, font=("Arial",11), widht=10, relief="solid", bd=1)
        self.txt_quantidade.grid(row=0, column=3, padx=5, pady=5)
        