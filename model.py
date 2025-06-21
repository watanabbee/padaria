import sqlite3 as sql
from datetime import datetime

class Produto:
    def __init__(self, nome, preco, ingredientes, modo_preparo, imagem):
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes
        self.modo_preparo = modo_preparo
        self.imagem = imagem


class Model:

    def __init__(self):
        self.conexao = sql.connect('padaria.db')
        self.criar_tabelas()
        self.contador = 0
        self.produtos = self.carregar_produtos()

    def carregar_produtos(self):
        return [
            Produto(
                nome="Misto Quente",
                preco = 1.50,
                ingredientes="Pão, presunto, queijo, orégano e manteiga.",
                modo_preparo="Com duas fatias de pão besuntamos ambas de manteiga, salpicamos o orégano "
                             "e colocamos duas fatias de queijo e presunto, finalizando dando o ponto na chapa.",
                imagem="imagens/misto.png"
            ),
            Produto(
                nome="Pão de Queijo",
                preco = 1.50,
                ingredientes="Polvilho, queijo, leite, ovos e óleo.",
                modo_preparo="Mistura-se todos os ingredientes até formar uma massa homogênea e assa-se até dourar.",
                imagem="imagens/misto.png"
            ),
                        Produto(
                nome="Misto Quente",
                preco = 1.50,
                ingredientes="Pão, presunto, queijo, orégano e manteiga.",
                modo_preparo="Com duas fatias de pão besuntamos ambas de manteiga, salpicamos o orégano "
                             "e colocamos duas fatias de queijo e presunto, finalizando dando o ponto na chapa.",
                imagem="imagens/misto.png"
            ),
            Produto(
                nome="Pão de Queijo",
                preco = 1.50,
                ingredientes="Polvilho, queijo, leite, ovos e óleo.",
                modo_preparo="Mistura-se todos os ingredientes até formar uma massa homogênea e assa-se até dourar.",
                imagem="imagens/misto.png"
            ),
                        Produto(
                nome="Misto Quente",
                preco = 1.50,
                ingredientes="Pão, presunto, queijo, orégano e manteiga.",
                modo_preparo="Com duas fatias de pão besuntamos ambas de manteiga, salpicamos o orégano "
                             "e colocamos duas fatias de queijo e presunto, finalizando dando o ponto na chapa.",
                imagem="imagens/misto.png"
            ),
            Produto(
                nome="Pão de Queijo",
                preco = 1.50,
                ingredientes="Polvilho, queijo, leite, ovos e óleo.",
                modo_preparo="Mistura-se todos os ingredientes até formar uma massa homogênea e assa-se até dourar.",
                imagem="imagens/misto.png"
            ),
                        Produto(
                nome="Misto Quente",
                preco = 1.50,
                ingredientes="Pão, presunto, queijo, orégano e manteiga.",
                modo_preparo="Com duas fatias de pão besuntamos ambas de manteiga, salpicamos o orégano "
                             "e colocamos duas fatias de queijo e presunto, finalizando dando o ponto na chapa.",
                imagem="imagens/misto.png"
            ),
            Produto(
                nome="Pão de Queijo",
                preco = 1.50,
                ingredientes="Polvilho, queijo, leite, ovos e óleo.",
                modo_preparo="Mistura-se todos os ingredientes até formar uma massa homogênea e assa-se até dourar.",
                imagem="imagens/misto.png"
            )
        ]

    def get_Produtos(self):
        return self.carregar_produtos()
    

    def incrementar_contador(self):
        self.contador += 1
    
    def criar_tabelas(self):
        cursor = self.conexao.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS cliques (id INTEGER PRIMARY KEY AUTOINCREMENT,timestamp TEXT NOT NULL)')
        cursor.execute('CREATE TABLE IF NOT EXISTS clientes (id_cliente INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, senha text not null, email text not null, idade int not null)')
        
        self.conexao.commit()

    def registrar_clique(self):
        cursor = self.conexao.cursor()
        timestamp = datetime.now().isoformat()
        cursor.execute('INSERT INTO cliques (timestamp) VALUES (?)', (timestamp,))
        self.conexao.commit()

    def get_Cliques(self):
        cursor = self.conexao.cursor()
        cursor.execute('SELECT COUNT(id) FROM cliques')
        resultado = cursor.fetchone()

        return resultado[0] if resultado else 0

    
    def set0_Cliques(self):

        cursor = self.conexao.cursor()
        cursor.execute('DELETE FROM cliques')
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='cliques'")
    
        self.conexao.commit()