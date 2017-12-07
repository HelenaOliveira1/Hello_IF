"""
    Publicação Orientado a Objeto
"""

import mysql
from database.Config_DB import *

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

class Publicacao():
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo

    def listar(self):
        publicacoes = []

        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM tb_publicacao;
        ''')
        for linha in cursor.fechall():
            tipo = linha[1]
            publicacao = Publicacao(tipo)
            publicacoes.append(publicacao)

        cursor.close()
        conn.close()

        return publicacoes

    def inserir(self):

        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        cursor.execute(''' INSERT INTO tb_publicacao(tipo) VALUES (?) ''', self.tipo)

        conn.commit()
        id = cursor.lastrowid
        cursor.close()
        conn.close()

        return id

    def deletar(self, id_mens):

        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        cursor.execute(''' DELETE FROM tb_publicacao WHERE id =? ''', (id_mens))

        conn.commit()
        cursor.close()
        conn.close()

    def __str__(self):
        return "Publicação <%i>" %(self.id)