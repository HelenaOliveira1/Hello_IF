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
        conn.close()

    def deletar(self, login_delt):

        conn = sqlite3.connect("hello_if.db")
        cursor.execute('''
            DELETE FROM tb_publicacao
            WHERE login =?        
            ''', login_delt)

        conn.comimit()
        conn.close()

  def atualizar(self, nova_senha, novo_login, novo_logado, novo_nome, nova_data_nasc, novo_genero, nova_profissao):
        conn = sqlite3.connect("hello_if.db")
        cursor.execute('''
            UPDATE tb_usuario
            SET nova_senha = ?, novo_login = ?, novo_logado = ?, novo_nome = ?, nova_data_nasc = ?, novo_genero = ?, nova_profissao = ?
            WHERE login=?
            ''', nova_senha, novo_login, novo_logado, novo_nome, nova_data_nasc, novo_genero, nova_profissao,self.login)

        conn.comimit()
        conn.close()
