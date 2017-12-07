"""
    Feed Orientado a Objeto
"""

import mysql
from database.Config_DB import *
from Model.Usuario import *
from Model.Mensagem import *

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

class Feed():

    def __init__(self, id, id_u, senha_u, login_u, logado_u, nome_u, data_nasc_u, genero_u, profissao_u, id_m, visibilidade, texto):
        self.id = id
        self.usuario = Usuario(id_u, senha_u, login_u, logado_u, nome_u, data_nasc_u, genero_u, profissao_u)
        self.mensagem = Mensagem(id_m, visibilidade, texto)

    def listar(self):

        publicacoes = []

        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        cursor.execute(''' SELECT * FROM tb_feed; ''')

        for linha in cursor.fechall():
            usuario = linha[1]
            mensagem = linha[2]
            lista_feed = Feed(usuario, mensagem)
            publicacoes.append(lista_feed)

        cursor.close()
        conn.close()

        return publicacoes

    def inserir(self):

        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO tb_feed(id, id_usuario, visib_mens) VALUES (?,?,?)
        ''', (self.id, self.usuario.id_u, self.mensagem.visibilidade))

        conn.commit()
        id = cursor.lastrowid
        cursor.close()
        conn.close()

        return id

    def deletar(self, id_mensagem):

        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        cursor.execute('''
            DELETE FROM tb_feed
            WHERE id =?
            ''', id_mensagem)

        conn.commit()
        cursor.close()
        conn.close()

    def atualizar(self, visib_mens):

        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE tb_feed
            SET visib_mens=?
            WHERE visib_mens=?
            ''', (visib_mens))

        conn.commit()
        cursor.close()
        conn.close()

    def __str__(self):
        return "Feed <%i>" %(self.id)