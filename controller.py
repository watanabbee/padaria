import tkinter as tk,view as v,model as m

class AppController:
    def __init__(self, root):
        self.root = root
        self.model = m.AppModel()
        self.tela1 = v.Tela1View(root, self)
        self.tela2 = v.Tela2View(root, self)
        self.tela_atual = None
        self.mudar_para_tela1()

    def mudar_para_tela1(self):
        self._mostrar_tela(self.tela1)

    def mudar_para_tela2(self):
        self._mostrar_tela(self.tela2)
        self.atualizar_contador_view()

    def incrementar_cliques(self):
        self.model.registrar_clique()
        self.atualizar_contador_view()

    def atualizar_contador_view(self):
        valor = self.model.contar_cliques()
        self.tela2.atualizar_contador(valor)

    def _mostrar_tela(self, tela):
        if self.tela_atual:
            self.tela_atual.pack_forget()
        self.tela_atual = tela
        self.tela_atual.pack(fill="both", expand=True)
# ---------------- MAIN ------------------
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Exemplo MVC com Contador")
    root.geometry("300x200")
    app = AppController(root)
    root.mainloop()