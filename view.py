import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import ttk
from Layoutview import LayoutBase



# ---------------- VIEW ------------------
class Tela1View(LayoutBase):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):

        frame_corpo = tk.Frame(self.frame_conteudo)
        frame_corpo.pack(expand=True, pady=20)
        frame_login = tk.LabelFrame(frame_corpo, text="Login", padx=10, pady=10)
        frame_login.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(frame_login, text="Email:").grid(row=0, column=0, sticky="e")
        tk.Label(frame_login, text="Senha:").grid(row=1, column=0, sticky="e")
        tk.Label(frame_login).grid(row=2, column=0, sticky="e")
        tk.Label(frame_login).grid(row=3, column=0, sticky="e")

        self.email_login_var = tk.StringVar()
        self.senha_login_var = tk.StringVar()

        tk.Entry(frame_login, textvariable=self.email_login_var).grid(row=0, column=1)
        tk.Entry(frame_login, textvariable=self.senha_login_var, show="*").grid(row=1, column=1)

        tk.Button(frame_login, text="Entrar").grid(row=4, column=0, columnspan=2, pady=5)

        frame_criar = tk.LabelFrame(frame_corpo, text="Criar Usuário", padx=10, pady=10)
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

        
        self.adicionar_botao_rodape("Seguir", comando=lambda: self.controller.gerenciador_telas(2), lado="right")

class Tela2View(LayoutBase):
    def __init__(self, master, controller, produtos):
        super().__init__(master)
        self.controller = controller
        self.produtos = produtos
        self.fotos = []
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self.frame_conteudo, text="Cardápio", bg="white",
                 font=("Arial", 18, "bold")).pack(pady=10)

        frame_busca = tk.Frame(self.frame_conteudo, bg="white", height=50)
        frame_busca.pack(fill="x", pady=5)

        tk.Label(frame_busca, text="Buscar:", bg="white", font=("Arial", 12)).pack(side="left", padx=10)
        self.busca_entry = tk.Entry(frame_busca, width=50)
        self.busca_entry.pack(side="left", padx=5)
        busca = self.busca_entry.get()

        tk.Button(frame_busca, text="Pesquisar", command=lambda: self.controller.filtrar_produtos(busca)).pack(side="left", padx=5)

        lista = tk.Frame(self.frame_conteudo, bg="white")
        lista.pack()

        for produto in self.produtos:
            frame = tk.Frame(lista, bd=1, relief="solid", bg="white", padx=5, pady=5)
            frame.pack(fill="x", pady=5)

            try:
                imagem = Image.open(produto.imagem).resize((60, 60), Image.LANCZOS)
                foto = ImageTk.PhotoImage(imagem)
                self.fotos.append(foto)
                tk.Label(frame, image=foto, bg="white").pack(side="left", padx=5)
            except Exception:
                tk.Label(frame, text="[Sem imagem]", bg="white").pack(side="left", padx=5)

            tk.Label(frame, text=produto.nome, bg="white", font=("Arial", 14)).pack(side="left", padx=10)

            tk.Button(frame, text="+", bg="#4CAF50", fg="white", width=3, height=1,
                      command=lambda p=produto: self.controller.mostrar_detalhes(p)).pack(side="right", padx=5)
        self.adicionar_botao_rodape("Voltar", comando=lambda: self.controller.gerenciador_telas(1), lado="left")
        self.adicionar_botao_rodape("Seguir", comando=lambda: self.controller.gerenciador_telas(3), lado="right")


    def carregar_imagem(self, caminho, tamanho=(80, 80)):
        try:
            imagem = Image.open(caminho).resize(tamanho, Image.LANCZOS)
            foto = ImageTk.PhotoImage(imagem)
            self.fotos.append(foto)  # Salvar referência
            return foto
        except Exception as e:
            print(f"Erro ao carregar {caminho}: {e}")
            return None
        
    def exibir_produtos(self, produtos):
        for widget in self.produtos_frame.winfo_children():
            widget.destroy()

        max_colunas = 3
        for index, produto in enumerate(produtos):
            linha = index // max_colunas
            coluna = index % max_colunas

            frame = tk.Frame(self.produtos_frame, bd=1, relief="solid", bg="white", padx=10, pady=10)
            frame.grid(row=linha, column=coluna, padx=15, pady=15, sticky="nsew")

            foto = self.carregar_imagem(produto.imagem)
            if foto:
                tk.Label(frame, image=foto, bg="white").pack(pady=5)
            else:
                tk.Label(frame, text="[Imagem]", bg="white").pack(pady=5)

            tk.Label(frame, text=produto.nome, bg="white", font=("Arial", 12, "bold")).pack()
            tk.Label(frame, text=f"R$ {produto.preco:.2f}", bg="white", font=("Arial", 10)).pack()
            tk.Button(frame, text="+", bg="#4CAF50", fg="white", width=3).pack(pady=5)

        for i in range(max_colunas):
            self.produtos_frame.grid_columnconfigure(i, weight=1)

        
class Tela2extendidaView(LayoutBase):

    def __init__(self, master, controller, produto):
        super().__init__(master)
        self.controller = controller
        self.produto = produto
        self.foto = None
        self.create_widgets()

    def create_widgets(self):



        frame = tk.Frame(self.frame_conteudo, bd=1, relief="solid", bg="white", padx=10, pady=10)
        frame.pack(fill="both", expand=True)

        # Título
        tk.Label(frame, text=self.produto.nome, bg="white", font=("Arial", 16, "bold")).grid(
            row=0, column=0, columnspan=2, sticky="w", padx=10, pady=5
        )

        # Imagem
        try:
            imagem = Image.open(self.produto.imagem).resize((150, 150), Image.LANCZOS)
            self.foto = ImageTk.PhotoImage(imagem)
            tk.Label(frame, image=self.foto, bg="white").grid(row=1, column=0, padx=10, pady=5)
        except Exception:
            tk.Label(frame, text="[Imagem não disponível]", bg="white").grid(row=1, column=0, padx=10, pady=5)

        tk.Label(frame, text="Imagem ilustrativa", bg="white", font=("Arial", 8, "italic")).grid(
            row=2, column=0, padx=10, sticky="n"
        )

        # Informações
        info = f"Ingredientes: {self.produto.ingredientes}\n\nModo de Preparo: {self.produto.modo_preparo}"
        tk.Label(frame, text=info, bg="white", justify="left", anchor="w", wraplength=400).grid(
            row=1, column=1, rowspan=2, sticky="nw", padx=10, pady=5
        )

        # Botão voltar
        self.adicionar_botao_rodape("Voltar", comando=lambda: self.controller.gerenciador_telas(2), lado="left")

class Tela3View(LayoutBase):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        frame_corpo = tk.Frame(self.frame_conteudo)
        frame_corpo.pack(expand=True, pady=20)

        self.contador_label = tk.Label(frame_corpo, text="Cliques: 0")
        self.contador_label.grid(row=0,column=0)

        btn_incrementar = tk.Button(frame_corpo, text="Clique aqui!", command=lambda:self.controller.incrementar_cliques())
        btn_incrementar.grid(row=1,column=0)


        self.adicionar_botao_rodape("Voltar", comando=lambda: self.controller.gerenciador_telas(2), lado="left")
        self.adicionar_botao_rodape("Seguir", comando=lambda: self.controller.gerenciador_telas(3), lado="right")


    def atualizar_contador(self, valor):
        self.contador_label.config(text=f"Cliques: {valor}")
