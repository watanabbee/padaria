import view as v
import model as m

class Controller:
    def __init__(self, root, model):
        self.root = root
        self.model = model

        # Telas estáticas (não dependem de dados dinâmicos)
        self.tela1 = v.Tela1View(root, self)
        self.tela2 = v.Tela2View(root, self)

        # Telas dinâmicas
        self.tela3 = None  # Lista de produtos
        self.tela4 = None  # Detalhe do produto

        self.tela_atual = None
        self.gerenciador_telas(1)

    def gerenciador_telas(self, id):
        if id == 1:
            self.mostrar_tela(self.tela1)
        elif id == 2:
            self.mostrar_tela(self.tela2)
            self.atualizar_contador_view()
        elif id == 3:
            self.mostrar_lista_produtos()
        elif id == 4:
            self.mostrar_tela(self.tela4)

    def mostrar_lista_produtos(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        produtos = self.model.carregar_produtos()
        self.tela3 = v.Tela3View(self.root, self, produtos)

        self.tela_atual = self.tela3
        self.tela_atual.pack(fill="both", expand=True)

    def mostrar_detalhes(self, produto):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela4 = v.Tela4View(self.root, self, produto)

        self.tela_atual = self.tela4
        self.tela_atual.pack(fill="both", expand=True)

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
