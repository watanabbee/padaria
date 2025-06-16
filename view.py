import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import ttk


# ---------------- VIEW ------------------
class Tela1View(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):

        frame_login = tk.LabelFrame(self, text="Login", padx=10, pady=10)
        frame_login.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(frame_login, text="Email:").grid(row=0, column=0, sticky="e")
        tk.Label(frame_login, text="Senha:").grid(row=1, column=0, sticky="e")

        self.email_login_var = tk.StringVar()
        self.senha_login_var = tk.StringVar()

        tk.Entry(frame_login, textvariable=self.email_login_var).grid(row=0, column=1)
        tk.Entry(frame_login, textvariable=self.senha_login_var, show="*").grid(row=1, column=1)

        tk.Button(frame_login, text="Entrar").grid(row=2, column=0, columnspan=2, pady=5)

        frame_criar = tk.LabelFrame(self, text="Criar Usuário", padx=10, pady=10)
        frame_criar.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frame_criar, text="Nome:").grid(row=0, column=0, sticky="e")
        tk.Label(frame_criar, text="Email:").grid(row=1, column=0, sticky="e")
        tk.Label(frame_criar, text="Idade:").grid(row=2, column=0, sticky="e")
        tk.Label(frame_criar, text="Senha:").grid(row=3, column=0, sticky="e")

        self.nome_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.idade_var = tk.StringVar()
        self.senha_var = tk.StringVar()

        tk.Entry(frame_criar, textvariable=self.nome_var).grid(row=0, column=1)
        tk.Entry(frame_criar, textvariable=self.email_var).grid(row=1, column=1)
        tk.Entry(frame_criar, textvariable=self.idade_var).grid(row=2, column=1)
        tk.Entry(frame_criar, textvariable=self.senha_var, show="*").grid(row=3, column=1)

        tk.Button(frame_criar, text="Criar Conta").grid(row=4, column=0, columnspan=2, pady=5)
        btn = tk.Button(self, text="Ir para Tela 2", command=lambda:self.controller.gerenciador_telas(2))
        btn.grid(row=1, column=0, columnspan=2, pady=10)

class Tela2View(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Tela 2")
        label.grid(row=0,column=0,padx=10,pady=10)

        self.contador_label = tk.Label(self, text="Cliques: 0")
        self.contador_label.grid(row=0,column=0)

        btn_incrementar = tk.Button(self, text="Clique aqui!", command=lambda:self.controller.incrementar_cliques())
        btn_incrementar.grid(row=1,column=0)

        btn_voltar = tk.Button(self, text="Voltar", command=lambda:self.controller.gerenciador_telas(1))
        btn_voltar.grid(row=2,column=2)
        btn_seguir = tk.Button(self, text="Ir para Tela 3", command=lambda:self.controller.gerenciador_telas(3))
        btn_seguir.grid(row=2,column=3)

    def atualizar_contador(self, valor):
        self.contador_label.config(text=f"Cliques: {valor}")

class Tela3View(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="white")
        self.controller = controller
        self.fotos = []
        self.create_widgets()

    def create_widgets(self):
        # ========== TOPO ==========
        frame_topo = tk.Frame(self, bg="#d2a679", height=80)
        frame_topo.pack(fill="x")

        tk.Label(frame_topo, text="Padaria VC++", bg="#d2a679", fg="black",
                 font=("Arial", 20, "bold")).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        tk.Label(frame_topo, text="Av. Das Padarias nº92", bg="#d2a679", fg="black",
                 font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=10)

        # ========== BUSCA ==========
        frame_busca = tk.Frame(self, bg="white", height=50)
        frame_busca.pack(fill="x", pady=5)

        tk.Label(frame_busca, text="Buscar:", bg="white", font=("Arial", 12)).pack(side="left", padx=10)
        self.busca_entry = tk.Entry(frame_busca, width=50)
        self.busca_entry.pack(side="left", padx=5)

        # ========== CONTEÚDO ==========
        frame_conteudo = tk.Frame(self, bg="white")
        frame_conteudo.pack(fill="both", expand=True, padx=10, pady=5)

        canvas = tk.Canvas(frame_conteudo, bg="white")
        scrollbar = ttk.Scrollbar(frame_conteudo, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        self.produtos_frame = tk.Frame(canvas, bg="white")
        self.produtos_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.produtos_frame, anchor="nw")

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # ========== RODAPÉ ==========
        frame_rodape = tk.Frame(self, bg="white", height=50)
        frame_rodape.pack(fill="x", pady=5)

        tk.Button(frame_rodape, text="Voltar", width=10, command=lambda: self.controller.gerenciador_telas(1)).pack(side="left", padx=10)
        tk.Button(frame_rodape, text="Seguir", width=10, command=lambda: self.controller.gerenciador_telas(4)).pack(side="right", padx=10)

    def exibir_produtos(self, produtos):
        for widget in self.produtos_frame.winfo_children():
            widget.destroy()

        max_colunas = 3
        for index, produto in enumerate(produtos):
            linha = index // max_colunas
            coluna = index % max_colunas

            frame = tk.Frame(self.produtos_frame, bd=1, relief="solid", bg="white", padx=10, pady=10)
            frame.grid(row=linha, column=coluna, padx=15, pady=15, sticky="nsew")

            try:
                imagem = Image.open(produto.imagem).resize((70, 70), Image.LANCZOS)
                foto = ImageTk.PhotoImage(imagem)
                self.fotos.append(foto)
                tk.Label(frame, image=foto, bg="white").pack(pady=5)
            except Exception as e:
                tk.Label(frame, text="[Erro imagem]", bg="white").pack(pady=5)

            tk.Label(frame, text=f"R$ {produto.preco:.2f}", bg="white", font=("Arial", 10)).pack()
            tk.Label(frame, text=produto.nome, bg="white", font=("Arial", 12)).pack()
            tk.Button(frame, text="+", bg="#4CAF50", fg="white", width=2, height=1).pack(pady=5)

        for i in range(max_colunas):
            self.produtos_frame.grid_columnconfigure(i, weight=1)
