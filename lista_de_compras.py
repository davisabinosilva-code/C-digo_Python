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
        self.txt_descricao = tk.Entry(frame_entrada, font=("Arial",11), widht=30, relief="solid", bd=1)
        self.txt_descricao.grid(row=0, column=1, padx=5, pady=5)
        
        # Quantidade
        tk.Label(frame_entrada, text="Quantidade: ", font=("Arial, 11"), bg="#f0f4f8", fg="#2c3e50").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.txt_quantidade = tk.Entry(frame_entrada, font=("Arial",11), widht=10, relief="solid", bd=1)
        self.txt_quantidade.grid(row=0, column=3, padx=5, pady=5)

        # Preço
        tk.Label(frame_entrada, text="Preço Unit. (R$): ", font=("Arial, 11"), bg="#f0f4f8", fg="#2c3e50").grid(row=0, column=4, padx=5, pady=5, sticky="e")
        self.txt_preco = tk.Entry(frame_entrada, font=("Arial",11), widht=12, relief="solid", bd=1)
        self.txt_preco.grid(row=0, column=5, padx=5, pady=5)

        # ============ FRAME DE BOTÕES ===============
        frame_botoes = tk.Frame(self.root, bg="#f0f4f8")
        frame_botoes.pack(pady=10)

        # Botão Inserir
        self.btn_inserir = tk.Button(
            frame_botoes,
            text="➕ Inserir",
            font=("Arial", 11, "bold"),
            bgg="#27ae60", fg="white",
            width=12, cursor="hand2",
            relief="flat",
            command=self.inserir
        )
        self.btn_inserir.pack(side="left", padx=5)
        
        # Botão Editar
        self.btn_editar = tk.Button(
            frame_botoes,
            text="✏️ Editar",
            font=("Arial", 11, "bold"),
            bg="#f39c12", fg="white",
            widht=12, cursor="hand2",
            relief="flat",
            command=self.editar
        )
        self.btn_editar.pack(side="left", pad=5)
        
        # Botão Deletar
        self.btn_deletar = tk.Button(
            frame_botoes,
            text="🗑️ Deletar",
            font=("Arial", 11, "bold"),
            bg="#e74c3c", fg="white",
            widht=12, cursor="hand2",
            relief="flat",
            command=self.deletar
        )
        self.btn_deletar.pack(side="left", pad=5)

        # Botão Limpar Campos
        self.btn_limpar = tk.Button(
            frame_botoes,
            text="🧹 Limpar",
            font=("Arial", 11, "bold"),
            bg="#7f8c8d", fg="white",
            widht=12, cursor="hand2",
            relief="flat",
            command=self.limpar_campos
        )
        self.btn_limpar.pack(side="left", pad=5)

        # =============== LISTA DE ITENS (TREEVIEW) ===============
        frame_lista = tk.Frame(self.root, bg="#f0f4f8")
        frame_lista.pack(pady=10, padx=20, fill="both", expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side="right", fill="y")

        # Treeview
        colunas = ("descricao", "quantidade", "preco", "subtotal")
        self.tree = ttk.Treeview(
            frame_lista,
            columns=colunas,
            show="headings",
            yscrollcommand=scrollbar.set,
            height=10
        )
        scrollbar.config(command=self.tree.yview)
        
        # Configurar colunas
        self.tree.heading("descricao", text="Descrição")
        self.tree.heading("quantidade", text="Qtd")
        self.tree.heading("preco", text="Preço Unit. (R$)")
        self.tree.heading("subtotal", text="Subtotal (R$)")
        
        self.tree.column("descricao", width=250, anchor="w")
        self.tree.column("quantidade", width=60, anchor="center")
        self.tree.column("preco", width=120, anchor="e")
        self.tree.column("subtotal", width=120, anchor="e")
        
        self.tree.pack(fill="both", expand=True)
        
        # Evento de seleção
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        
        # ========== TOTAL =========
        frame_total = tk.Frame(self.root, bg="#f0f4f8")
        frame_total.pack(pady=10, padx=20, fill="x")
        
        self.lbl_total = tk.Label(
            frame_total,
            text="TOTAL: R$0,00",
            font=("Arial", 16, "bold"),
            bg="#f0f4f8",
            fg="#1a5276"
        )
        self.lbl_total.pack(side="right")
        
        # ========== STATUS BAR =========
        self.lbl_status = tk.label(
            self.root,
            text="Pronto. Selecione um item para editar ou deletar.",
            font=("Arial", 9),
            bg="#d5dbdb",
            fg="#2c3e50",
            anchor="w"
        )
        self.lbl_status.pack(fill="x", side="bottom")
        

