import view as v


class Controller:
    def __init__(self, root, model):
        self.root = root
        self.model = model

        self.tela1 = v.Tela1View(root, self)
        self.tela2 = v.Tela2View(self.root,self, self.model.carregar_produtos())
        self.tela3 = v.Tela3View(root, self)
        self.tela_atual = None
        self.gerenciador_telas(1)
        self.produtos = self.model.carregar_produtos()

    def gerenciador_telas(self, id):
        if id == 1:
            self.mostrar_tela(self.tela1)
        elif id == 2:
            self.mostrar_tela(self.tela2)
        elif id == 3:
            self.atualizar_contador_view()
            self.mostrar_tela(self.tela3)


    def mostrar_lista_produtos(self):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        produtos = self.model.carregar_produtos()
        self.tela2 = v.Tela2View(self.root,self, produtos)

        self.tela_atual = self.tela3
        self.tela_atual.pack(fill="both", expand=True)

    def filtrar_produtos(self, termoBusca):
        termoBusca = termoBusca.lower()
        produtos_filtrados = [p for p in self.produtos if termoBusca in p.nome.lower()]
        self.exibir_produtos(produtos_filtrados)

    def mostrar_detalhes(self, produto):
        self.tela2extendida = v.Tela2extendidaView(self.root, self, produto)
        self.mostrar_tela(self.tela2extendida)

    def mostrar_tela(self, tela):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = tela
        self.tela_atual.pack(fill="both", expand=True)

    def atualizar_contador_view(self):
        valor = self.model.contar_cliques()
        self.tela3.atualizar_contador(valor)

    def incrementar_cliques(self):
        self.model.registrar_clique()
        self.atualizar_contador_view()
