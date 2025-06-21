import tkinter as tk

class LayoutBase(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")
        

        # Topo
        self.frame_topo = tk.Frame(self, bg="#d2a679", height=80)
        self.frame_topo.pack(fill="x")
        tk.Label(self.frame_topo, text="Padaria VC++", bg="#d2a679", fg="black",
                 font=("Arial", 20, "bold")).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        tk.Label(self.frame_topo, text="Av. Das Padarias nº92", bg="#d2a679", fg="black",
                 font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=10)

        # Conteúdo
        self.frame_conteudo = tk.LabelFrame(self, bg="white")
        self.frame_conteudo.pack(fill="both", expand=True, padx=20, pady=40)

        # Rodapé
        self.frame_rodape = tk.Frame(self, bg="white", height=50)
        self.frame_rodape.pack(fill="x", pady=5)

    def adicionar_botao_rodape(self, texto, comando, lado="left"):
        tk.Button(self.frame_rodape, text=texto, width=10, command=comando).pack(side=lado, padx=10)
