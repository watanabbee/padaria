import view as v,time as t


class Controller:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.inicio = None
        self.rodando = False
        self.misto_comidos = 0

        self.tela1 = v.Tela1View(root, self)
        self.tela2 = v.Tela2View(self.root,self, self.model.carregar_produtos())
        self.tela3 = v.Tela3View(root, self)
        self.telaJogo = v.TelaJogo(root, self)
        self.telaJogoExtendida = v.TelaJogoExtendida(root,self)

        self.tela_atual = None
        self.gerenciador_telas(4)
        self.produtos = self.model.carregar_produtos()
        

    def gerenciador_telas(self, id):
        if id == 1:
            self.mostrar_tela(self.tela1)
        elif id == 2:
            self.mostrar_tela(self.tela2)
        elif id == 3:
            self.mostrar_tela(self.tela3)
        elif id==4:
            self.model.set0_Cliques()
            self.telaJogo.atualizar_imagem()
            self.resetar_cronometro()
            self.mostrar_tela(self.telaJogo)
            self.iniciar_cronometro()
        elif id ==5:
            self.parar_cronometro()
            self.mostrar_tela(self.telaJogoExtendida)
            self.telaJogoExtendida.set_score()
            self.telaJogoExtendida.set_imagemFinal()

    def getProduto(self):
        self.produtos = self.model.carregar_produtos()
        return self.produtos

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
        self.tela2.exibir_produtos(produtos_filtrados)

    def mostrar_detalhes(self, produto):
        self.tela2extendida = v.Tela2extendidaView(self.root, self, produto)
        self.mostrar_tela(self.tela2extendida)

    def mostrar_tela(self, tela):
        if self.tela_atual:
            self.tela_atual.pack_forget()

        self.tela_atual = tela
        self.tela_atual.pack(fill="both", expand=True)

    def iniciar_cronometro(self):
        if not hasattr(self, 'rodando'):
            self.rodando = False
        if not hasattr(self, 'inicio'):
            self.inicio = None

        if not self.rodando:
            if self.inicio is None:
                self.inicio = t.time()
            self.rodando = True
            self.atualizar_cronometro()

    def atualizar_cronometro(self):

        if self.rodando:
            tempo = t.time() - self.inicio
            self.telaJogo.atualizar_tempo(tempo)
            self.root.after(100, self.atualizar_cronometro)

    def parar_cronometro(self):
        if self.rodando:
            self.tempo_final = t.time() - self.inicio
            self.rodando = False

    def get_tempo_final(self):
        return getattr(self, 'tempo_final', 0)

    def resetar_cronometro(self):
        self.rodando = False
        self.inicio = None
        self.telaJogo.atualizar_tempo(0)

    def get_CaminhoJogo(self):
        
        x = self.model.get_Cliques()
        if x >= 28:
            self.misto_comidos+=1
            self.telaJogo.atualizar_mistoQuentes(self.misto_comidos)
            self.model.set0_Cliques()

        caminho = f"imagens/misto{round(x/2)}.png"
        return caminho
    
    def get_mistoComidos(self):
        misto_comidos = self.misto_comidos
        return misto_comidos

    def atualizar_contador_view(self):
        valor = self.model.get_Cliques()
        self.telaJogo.atualizar_contador(valor)

    def incrementar_cliques(self):
        self.model.registrar_clique()
        self.atualizar_contador_view()
