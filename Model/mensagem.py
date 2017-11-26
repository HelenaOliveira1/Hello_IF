"""
    Mensagem Orientado a Objeto
"""

import sqlite3

conn = sqlite3.connect("hello_if.db")
cursor = conn.cursor()

class Mensagem():

    def __init__(self, id, visibilidade, texto):
        self.id = id
        self.visibilidade = visibilidade
        self.texto = texto

    def listar(self):
        mensagens = []

        conn = sqlite3.connect("hello_if.db")
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM tb_mensagem;
        ''')
        for linha in cursor.fechall():
            visibilidade = linha[1]
            texto = linha[2]
            mensagem = Mensagem(visibilidade, texto)
            mensagens.append(mensagem)

        conn.close()

        return mensagens

    def inserir(self):
        conn = sqlite3.connect("hello_if.db")
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO tb_mensagem(visibilidade, texto) VALUES (?,?)
        ''', (self.visibilidade, self.texto))

        conn.commit()
        id = cursor.lastrowid
        conn.close()
        
        return id

    def deletar(self, id_mens):

        conn = sqlite3.connect("hello_if.db")
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM tb_mensagem
            WHERE id =?
            ''', id_mens)

        conn.commit()
        conn.close()
