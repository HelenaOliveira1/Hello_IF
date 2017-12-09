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
        try:

            publicacoes = []

            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            cursor.execute(''' SELECT * FROM tb_feed; ''')

            for linha in cursor.fechall():
                usuario = linha[1]
                mensagem = linha[2]
                lista_feed = Feed(usuario, mensagem)
                publicacoes.append(lista_feed)
            return publicacoes
        except:
            print("Ocorreu um ERRO!")
        finally:
            cursor.close()
            conn.close()

    def inserir(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO tb_feed(id, id_usuario, visib_mens) VALUES (?,?,?)
            ''', (self.id, self.usuario.id_u, self.mensagem.visibilidade))

            conn.commit()
            id = cursor.lastrowid
            return id
        except:
           print("Ocorreu um ERRO!")
        finally:
            cursor.close()
            conn.close()

    def deletar(self, id_mensagem):
        try:

            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            cursor.execute('''
                DELETE FROM tb_feed
                WHERE id =?
                ''', id_mensagem)

            conn.commit()
        except:
           print("Ocorreu um ERRO!")
        finally:
            cursor.close()
            conn.close()

    def atualizar(self, visib_mens):
        try:

            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            cursor.execute('''
                UPDATE tb_feed
                SET visib_mens=?
                WHERE visib_mens=?
                ''', (visib_mens))

            conn.commit()
        except:
           print("Ocorreu um ERRO!")
        finally:
            cursor.close()
            conn.close()

    def __str__(self):
        return "Feed <%i>" %(self.id)
