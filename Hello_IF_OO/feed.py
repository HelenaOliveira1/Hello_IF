"""
    Feed Orientado a Objeto
"""

from Hello_IF_OO.mensagem import Mensagem
from Hello_IF_OO.usuario import Usuario
import sqlite3

conn = sqlite3.connect("hello_if.db")
cursor = conn.cursor()

class Feed():

    def __init__(self, id, id_u, senha_u, login_u, logado_u, nome_u, data_nasc_u, genero_u, profissao_u, id_m, visibilidade, texto):
        self.id = id
        self.usuario = Usuario(id_u, senha_u, login_u, logado_u, nome_u, data_nasc_u, genero_u, profissao_u)
        self.mensagem = Mensagem(id_m, visibilidade, texto)

    def listar(self):

        publicacoes = []
        conn = sqlite3.connect("hello_if.db")
        cursor = conn.cursor()

        cursor.execute('''
            #SELECT * FROM tb_feed;
        ''')
        for linha in cursor.fechall():
            usuario = linha[1]
            mensagem = linha[2]
            lista_feed = Feed(usuario, mensagem)
            publicacoes.append(lista_feed)

        conn.close()

        return publicacoes

    def inserir(self):

        conn = sqlite3.connect("hello_if.db")
        cursor = conn.cursor()
        cursor.execute('''
            #INSERT INTO tb_feed(id, id_usuario, visib_mens) VALUES (self.id, self.usuario.id_u, self.mensagem.visibilidade)
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
        
