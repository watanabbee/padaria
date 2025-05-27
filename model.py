import sqlite3 as sql
from datetime import datetime


class AppModel:

    def __init__(self):
        self.data = "Algum dado do modelo"
        self.conexao = sql.connect('padaria.db')
        self.criar_tabelas()

        self.contador = 0

    def incrementar_contador(self):
        self.contador += 1

    def obter_contador(self):
        return self.contador
    
    def criar_tabelas(self):
        cursor = self.conexao.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS cliques (id INTEGER PRIMARY KEY AUTOINCREMENT,timestamp TEXT NOT NULL)')
        cursor.execute('CREATE TABLE IF NOT EXISTS clientes (id_cliente INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, senha text not null)')
        
        self.conexao.commit()


    def registrar_clique(self):
        cursor = self.conexao.cursor()
        timestamp = datetime.now().isoformat()
        cursor.execute('INSERT INTO cliques (timestamp) VALUES (?)', (timestamp,))
        self.conexao.commit()

    def contar_cliques(self):
        cursor = self.conexao.cursor()
        cursor.execute('SELECT COUNT(id) FROM cliques')
        resultado = cursor.fetchone()
        return resultado[0] if resultado else 0