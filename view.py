import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import ttk
from Layoutview import LayoutBase



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

class Tela2View(LayoutBase):
    def __init__(self, master, controller):
        super().__init__(master,controller)
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Tela 2")
        label.pack()

        self.contador_label = tk.Label(self, text="Cliques: 0")
        self.contador_label.pack()

        btn_incrementar = tk.Button(self, text="Clique aqui!", command=lambda:self.controller.incrementar_cliques())
        btn_incrementar.pack()

        btn_voltar = tk.Button(self, text="Voltar", command=lambda:self.controller.gerenciador_telas(1))
        btn_voltar.pack()
        btn_seguir = tk.Button(self, text="Ir para Tela 3", command=lambda:self.controller.gerenciador_telas(3))
        btn_seguir.pack()

    def atualizar_contador(self, valor):
        self.contador_label.config(text=f"Cliques: {valor}")

class Tela3View(LayoutBase):
    def __init__(self, master, controller, produtos):
        super().__init__(master, controller)
        self.produtos = produtos
        self.fotos = []
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.frame_conteudo, text="Cardápio", bg="white",
                 font=("Arial", 18, "bold")).pack(pady=10)

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

class Tela4View(LayoutBase):

    def __init__(self, master, controller, produto):
        super().__init__(master, controller)
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
        self.adicionar_botao_rodape("Voltar", comando=lambda: self.controller.mostrar_lista_produtos())

