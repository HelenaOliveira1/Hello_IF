"""
    Chat Orientado a Objeto
"""

import sqlite3
from Model.usuario import Usuario
from Model.mensagem import Mensagem

conn = sqlite3.connect("hello_if.db")
cursor = conn.cursor()

class Chat():
    def __init__(self, id, id_u, senha_u, login_u, logado_u, nome_u, data_nasc_u, genero_u, profissao_u, id_a, senha_a,
                 login_a, logado_a, nome_a, data_nasc_a, genero_a, profissao_a, id_m, visibilidade, texto):
        self.id = id
        self.usuario = Usuario(id_u, senha_u, login_u, logado_u, nome_u, data_nasc_u, genero_u, profissao_u)
        self.amigo = Usuario(id_a, senha_a, login_a, logado_a, nome_a, data_nasc_a, genero_a, profissao_a)
        self.mensagem = Mensagem(id_m, visibilidade, texto)

    def listar(self):
        mensagens = []

        conn = sqlite3.connect("hello_if.db")
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM tb_mensagem;
        ''')
        for linha in cursor.fechall():
            usuario = linha[1]
            amigo = linha[2]
            mensagem = linha[3]
            lista_mensagens = Chat(usuario, amigo, mensagem)
            mensagens.append(lista_mensagens)

        conn.close()

        return mensagens

    def inserir(self):
        
        conn = sqlite3.connect("hello_if.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tb_mensagem(id, id_usuario, visib_mens, id_usuario_amigo) VALUES (self.id, self.usuario.id_u, self.mensagem.visibilidade, self.amigo.id_a)
        ''')

        conn.commit()
        id = cursor.lastrowid
        conn.close()
        
        return id

    def deletar(self, id_delt):

        conn = sqlite3.connect("hello_if.db")
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM tb_chat
            WHERE id =?
            ''', id_delt)

        conn.commit()
        conn.close()
