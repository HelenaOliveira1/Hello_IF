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
            INSERT INTO tb_mensagem(visibilidade, texto) VALUES (self.visibilidade, self.texto)
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
