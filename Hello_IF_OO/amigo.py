"""
    Amigo Orientado a Objeto
"""

from Hello_IF_OO.usuario import Usuario
import sqlite3

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
            #SELECT * FROM tb_amigo;
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
            #INSERT INTO tb_amigo(id, id_usuario, id_usuario_amigo) VALUES (self.id, self.usuario.id_u, self.amigo.id_a)
        ''')

        conn.commit()
        conn.close()

     def deletar(self, login_delt):

        conn = sqlite3.connect("hello_if.db")
        cursor.execute('''
            DELETE FROM tb_amigo
            WHERE login =?        
            ''', login_delt)

        conn.commit()
        conn.close()

  def atualizar(self, nova_senha, novo_login, novo_logado, novo_nome, nova_data_nasc, novo_genero, nova_profissao, login):
        conn = sqlite3.connect("hello_if.db")
        cursor.execute('''
            UPDATE tb_amigo
            SET nova_senha = ?, novo_login = ?, novo_logado = ?, novo_nome = ?, nova_data_nasc = ?, novo_genero = ?, nova_profissao = ?
            WHERE login=?
            ''', (nova_senha, novo_login, novo_logado, novo_nome, nova_data_nasc, novo_genero, nova_profissao,login))

        conn.commit()
        conn.close()
