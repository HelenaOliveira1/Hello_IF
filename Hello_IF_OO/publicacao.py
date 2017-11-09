"""
    Publicação Orientado a Objeto
"""

import sqlite3

conn = sqlite3.connect("hello_if.db")
cursor = conn.cursor()

class Publicacao():
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo

    def listar(self):
        publicacoes = []

        conn = sqlite3.connect("hello_if.db")
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM tb_publicacao;
        ''')
        for linha in cursor.fechall():
            tipo = linha[1]
            publicacao = Publicacao(tipo)
            publicacoes.append(publicacao)

        conn.close()

        return publicacoes

    def inserir(self):
        conn = sqlite3.connect("hello_if.db")
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO tb_publicacao(tipo) VALUES (self.tipo)
        ''')

        conn.commit()
        id = cursor.lastrowid
        conn.close()
        
        return id

    def deletar(self, visib_mens):

        conn = sqlite3.connect("hello_if.db")
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM tb_publicacao
            WHERE visib_mens =?        
            ''', (visib_mens))

        conn.commit()
        conn.close()
