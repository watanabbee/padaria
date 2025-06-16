import tkinter as tk,view as v,model as m

class Controller:
    def __init__(self, root):
        self.root = root
        self.model = m.Model()
        self.tela1 = v.Tela1View(root, self)
        self.tela2 = v.Tela2View(root, self)
        self.tela3 = v.Tela3View(root, self)
        self.tela_atual = None
        self.gerenciador_telas(1)

    def gerenciador_telas(self,id):
        if id==1:
            self.mostrar_tela(self.tela1)
        elif id==2:
            self.mostrar_tela(self.tela2)
            self.atualizar_contador_view()
        elif id==3:
            self.mostrar_tela(self.tela3)
            self.mostrar_produtos()



    def mostrar_produtos(self):
        produtos = self.model.carregar_produtos()
        self.tela3.exibir_produtos(produtos)

    #def login_criar(self):

    def mostrar_tela(self, tela):
        if self.tela_atual:
            self.tela_atual.pack_forget()
        self.tela_atual = tela
        self.tela_atual.pack(fill="both", expand=True)
    
    def atualizar_contador_view(self):
        valor = self.model.contar_cliques()
        self.tela2.atualizar_contador(valor)

    def incrementar_cliques(self):
        self.model.registrar_clique()
        self.atualizar_contador_view()

# ---------------- MAIN ------------------
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Exemplo MVC com Contador")
    root.geometry("500x500")
    isso = Controller(root)
    root.mainloop()