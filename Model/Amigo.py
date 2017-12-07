"""
    Amigo Orientado a Objeto
"""

from Model.Usuario import *
import mysql
from database.Config_DB import *

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

class Amigo():

    def __init__(self, id, id_u, senha_u, login_u, logado_u, nome_u, data_nasc_u, genero_u, profissao_u, id_a, senha_a, login_a, logado_a, nome_a, data_nasc_a, genero_a, profissao_a):
        self.id = id
        self.usuario = Usuario(id_u, senha_u, login_u, logado_u, nome_u, data_nasc_u, genero_u, profissao_u)
        self.amigo = Usuario(id_a, senha_a, login_a, logado_a, nome_a, data_nasc_a, genero_a, profissao_a)

    def listar(self):

        amigos = []

        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM tb_amigo;
        ''')
        for linha in cursor.fechall():
            usuario = linha[1]
            amigo = linha[2]
            lista_amigo = Amigo(usuario, amigo)
            amigos.append(lista_amigo)

        cursor.close()
        conn.close()

        return amigos

    def inserir(self):

        conn = mysql.conncetor.connect(**config)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tb_amigo(id, id_usuario, id_usuario_amigo) VALUES (?,?,?)
        ''',(self.id, self.usuario.id_u, self.amigo.id_a))

        conn.commit()
        id = cursor.lastrowid
        cursor.close()
        conn.close()

        return id

    def deletar(self, id_delt):

        conn = mysql.conncetor.connect(**config)
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM tb_amigo
            WHERE id =?
            ''', id_delt)

        conn.commit()
        conn.close()

    def __str__(self):
        return "Amigo <%s>" %(self.nome)

    def __repr__(self):
        return self.__str__()