"""
    Mensagem Orientado a Objeto
"""

import mysql
from database.Config_DB import *

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

class Mensagem():

    def __init__(self, id, visibilidade, texto):
        self.id = id
        self.visibilidade = visibilidade
        self.texto = texto

    def listar(self):
        mensagens = []

        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM tb_mensagem;
        ''')
        for linha in cursor.fechall():
            visibilidade = linha[1]
            texto = linha[2]
            mensagem = Mensagem(visibilidade, texto)
            mensagens.append(mensagem)

        cursor.close()
        conn.close()

        return mensagens

    def inserir(self):

        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO tb_mensagem(visibilidade, texto) VALUES (?,?)
        ''', (self.visibilidade, self.texto))

        conn.commit()
        id = cursor.lastrowid
        cursor.close()
        conn.close()

        return id

    def deletar(self, id_mens):

        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute(''' DELETE FROM tb_mensagem WHERE id =? ''', id_mens)

        conn.commit()
        cursor.close()
        conn.close()

    def __str__(self):
        return "Mensagem <%i>" %(self.id)