"""
    Amigo Orientado a Objeto
"""

import sqlite3
from Model.usuario import *

conn = sqlite3.connect("hello_if.db")
cursor = conn.cursor()

class Amigo():

    def __init__(self, id, id_u, senha_u, login_u, logado_u, nome_u, data_nasc_u, genero_u, profissao_u, id_a, senha_a, login_a, logado_a, nome_a, data_nasc_a, genero_a, profissao_a):
        self.id = id
        self.usuario = Usuario(id_u, senha_u, login_u, logado_u, nome_u, data_nasc_u, genero_u, profissao_u)
        self.amigo = Usuario(id_a, senha_a, login_a, logado_a, nome_a, data_nasc_a, genero_a, profissao_a)

    def listar(self):

        amigos = []

        conn = sqlite3.connect("hello_if.db")
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM tb_amigo;
        ''')
        for linha in cursor.fechall():
            usuario = linha[1]
            amigo = linha[2]
            lista_amigo = Amigo(usuario, amigo)
            amigos.append(lista_amigo)

        conn.close()

        return amigos

    def inserir(self):

        conn = sqlite3.connect("hello_if.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tb_amigo(id, id_usuario, id_usuario_amigo) VALUES (self.id, self.usuario.id_u, self.amigo.id_a)
        ''')

        conn.commit()
        id = cursor.lastrowid
        conn.close()
        
        return id

    def deletar(self, id_delt):

        conn = sqlite3.connect("hello_if.db")
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM tb_amigo
            WHERE id =?
            ''', id_delt)

        conn.commit()
        conn.close()
