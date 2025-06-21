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
        self.exibir_produtos(self.produtos)

        
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
        
        frame_conteudo = tk.Frame(self.frame_conteudo, bg="white")
        frame_conteudo.pack(fill="both", expand=True, padx=10, pady=5)

        canvas = tk.Canvas(self.frame_conteudo, bg="white")
        scrollbar = ttk.Scrollbar(self.frame_conteudo, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        self.produtos_frame = tk.Frame(canvas, bg="white")
        self.produtos_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.produtos_frame, anchor="nw")

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

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
            tk.Button(frame, text="+", bg="#4CAF50", fg="white", width=3,
                      command=lambda p=produto: self.controller.mostrar_detalhes(p)).pack(pady=5)

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

        try:
            imagem = Image.open(self.produto.imagem).resize((150, 150), Image.LANCZOS)
            self.foto = ImageTk.PhotoImage(imagem)
            tk.Label(frame, image=self.foto, bg="white").grid(row=1, column=0, padx=10, pady=5)
        except Exception:
            tk.Label(frame, text="[Imagem não disponível]", bg="white").grid(row=1, column=0, padx=10, pady=5)

        tk.Label(frame, text="Imagem ilustrativa", bg="white", font=("Arial", 8, "italic")).grid(
            row=2, column=0, padx=10, sticky="n"
        )

        info = f"Ingredientes: {self.produto.ingredientes}\n\nModo de Preparo: {self.produto.modo_preparo}"
        tk.Label(frame, text=info, bg="white", justify="left", anchor="w", wraplength=400).grid(
            row=1, column=1, rowspan=2, sticky="nw", padx=10, pady=5
        )

        self.adicionar_botao_rodape("Voltar", comando=lambda: self.controller.gerenciador_telas(2), lado="left")


class Tela3View(LayoutBase):
    def __init__(self, master,controller):
        super().__init__(master)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        
        # Definindo dois containers principais: Esquerda (cupons) e Direita (jogo)
        self.frame_conteudo.grid_columnconfigure(0, weight=1)
        self.frame_conteudo.grid_columnconfigure(1, weight=1)
        self.frame_conteudo.grid_rowconfigure(0, weight=1)

        # ----- Container Esquerdo -----
        container_esquerdo = tk.Frame(self.frame_conteudo, bg="white")
        container_esquerdo.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)

        container_esquerdo.grid_rowconfigure(0, weight=1)  # Parte texto + botões
        container_esquerdo.grid_rowconfigure(1, weight=0)  # Botão "Meus Cupons"
        container_esquerdo.grid_columnconfigure(0, weight=1)

        # Texto informativo
        tk.Label(container_esquerdo, text="Interessado em ganhar até\n20% de desconto em suas\ncompras físicas?",
                 bg="white", font=("Arial", 11), justify="left").grid(row=0, column=0, sticky="nw", pady=(0, 10))

        # Frame para botões de desconto
        frame_botoes = tk.Frame(container_esquerdo, bg="white")
        frame_botoes.grid(row=0, column=0, sticky="s", pady=(60, 0))

        frame_botoes.grid_columnconfigure(0, weight=1)
        frame_botoes.grid_columnconfigure(1, weight=1)

        descontos = ["5% OFF", "8% OFF", "10% OFF",
                     "14% OFF", "17% OFF", "20% OFF"]

        for i, desc in enumerate(descontos):
            btn = tk.Button(frame_botoes, text=desc, bg="#FFD700",
                            width=10, height=2)
            btn.grid(row=i // 2, column=i % 2, padx=5, pady=5, sticky="nsew")

        # Botão "Meus Cupons" centralizado na parte inferior
        tk.Button(container_esquerdo, text="Meus Cupons", width=15,
                  relief="solid").grid(row=1, column=0, pady=10)


        # ----- Container Direito -----
        container_direito = tk.Frame(self.frame_conteudo, bg="white")
        container_direito.grid(row=0, column=1, sticky="nsew", padx=20, pady=10)

        container_direito.grid_rowconfigure(0, weight=1)
        container_direito.grid_rowconfigure(1, weight=0)
        container_direito.grid_columnconfigure(0, weight=1)

        # Texto superior
        tk.Label(container_direito, text="Então coma todos os Mistos\nQuentes possíveis!",
                 bg="white", font=("Arial", 11), justify="center").grid(row=0, column=0, sticky="n", pady=(0, 10))

        # Frame da imagem
        frame_imagem = tk.Frame(container_direito, bg="white")
        frame_imagem.grid(row=0, column=0, sticky="n", pady=(60, 0))

        try:
            imagem = Image.open("imagens/misto.png")
            imagem = imagem.resize((240, 200), Image.LANCZOS)
            self.foto = ImageTk.PhotoImage(imagem)
            tk.Label(frame_imagem, image=self.foto, bg="white").pack()
        except:
            tk.Label(frame_imagem, text="[Imagem]", bg="white").pack()

        # Botão "Jogar" centralizado na parte inferior
        tk.Button(container_direito, text="Jogar", command = lambda: self.controller.gerenciador_telas(4), bg="#00cc00", fg="white",
                  width=15).grid(row=1, column=0, pady=10)

        self.adicionar_botao_rodape("Voltar", comando=lambda: self.controller.gerenciador_telas(2), lado="left")
    
class TelaJogo(LayoutBase):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.controller.iniciar_cronometro()
        self.create_widgets()

    def create_widgets(self):
        self.frame_corpo = tk.Frame(self.frame_conteudo)
        self.frame_corpo.pack(expand=True, pady=20)

        self.label_imagem = tk.Label(self.frame_corpo,text="mistos quentes comidos: ")
        self.label_imagem.grid(row=0,column=0)
        self.botao_imagem = None
        self.contador_label = tk.Label(self.frame_corpo,text="Cliques: 0")
        self.cronometro_label = tk.Label(self.frame_corpo,text="Tempo : 0")

        self.adicionar_botao_rodape("Voltar", comando=lambda: self.controller.gerenciador_telas(2), lado="left")
        self.adicionar_botao_rodape("Seguir", comando=lambda: self.controller.gerenciador_telas(3), lado="right")

    def atualizar_tempo(self):
        self.tempo = self.controller.get_time()
        try:
            self.cronometro_label = tk.Label(self.frame_corpo, text=f"Tempo: {self.tempo:.2f} segundos")
        except:
            self.cronometro_label = tk.Label(self.frame_corpo, text=f"Tempo: 0.00 segundos")
        self.cronometro_label.grid(row=2,column=0)

    def atualizar_contador(self, valor):
        self.contador_label.config(text=f"Cliques: {valor}")
        self.contador_label.grid(row=3,column=0)
        self.atualizar_imagem()
    
    def atualizar_imagem(self):

        caminho = self.controller.get_CaminhoJogo()

        try:
            img = Image.open(caminho)
            img = img.resize((200, 150))
            self.foto = ImageTk.PhotoImage(img)

            if self.botao_imagem:
                self.botao_imagem.config(image=self.foto)
            else:
                self.botao_imagem = tk.Button(
                    self.frame_corpo, image=self.foto, command=lambda: (self.acao_botao_imagem()),
                    borderwidth=0, highlightthickness=0, bg="white", activebackground="white"
                )
                self.botao_imagem.grid(row=1,column=0)

        except Exception as e:
            print(f"Erro ao carregar {caminho}: {e}")
            if self.botao_imagem:
                self.botao_imagem.destroy()
            self.label_imagem.config(text="Imagem não encontrada", image="")
        
    def acao_botao_imagem(self):
        self.controller.incrementar_cliques()
        self.atualizar_imagem()

            