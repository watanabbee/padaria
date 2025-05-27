import tkinter as tk
import controller as c


# ---------------- VIEW ------------------
class Tela1View(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):


        label = tk.Label(self, text="Tela 1")
        label.pack(pady=10)
        btn = tk.Button(self, text="Ir para Tela 2", command=self.controller.mudar_para_tela2)
        btn.pack()

class Tela2View(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Tela 2")
        label.pack(pady=10)

        self.contador_label = tk.Label(self, text="Cliques: 0")
        self.contador_label.pack(pady=10)

        btn_incrementar = tk.Button(self, text="Clique aqui!", command=self.controller.incrementar_cliques)
        btn_incrementar.pack(pady=5)

        btn_voltar = tk.Button(self, text="Voltar para Tela 1", command=self.controller.mudar_para_tela1)
        btn_voltar.pack(pady=5)

    def atualizar_contador(self, valor):
        self.contador_label.config(text=f"Cliques: {valor}")