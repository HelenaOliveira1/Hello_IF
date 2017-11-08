"""
    Chat Orientado a Objeto
"""

from Hello_IF_OO.usuario import Usuario
from Hello_IF_OO.mensagem import Mensagem
import sqlite3

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
            #SELECT * FROM tb_mensagem;
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
            #INSERT INTO tb_mensagem(id, id_usuario, visib_mens, id_usuario_amigo) VALUES (self.id, self.usuario.id_u, self.mensagem.visibilidade, self.amigo.id_a)
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
        
