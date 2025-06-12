import tkinter as tk,controller as c
from PIL import Image, ImageTk



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
        super().__init__(master)
        self.controller = controller
        self.create_widgets()   

    def create_widgets(self):
        label = tk.Label(self, text="Tela 3")
        label.grid(row=0,column=0,padx=10,pady=10)
        btn_voltar = tk.Button(self, text="Voltar", command=lambda: self.controller.gerenciador_telas(2))
        btn_voltar.grid(row=2,column=2)
