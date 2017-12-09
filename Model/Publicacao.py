"""
    Publicação Orientado a Objeto
"""

import mysql
from database.Config_DB import *

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

class Publicacao():
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo

    def listar(self):
        try:
            publicacoes = []

            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            cursor.execute('''
                SELECT * FROM tb_publicacao;
            ''')
            for linha in cursor.fechall():
                tipo = linha[1]
                publicacao = Publicacao(tipo)
                publicacoes.append(publicacao)
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

            cursor.execute(''' INSERT INTO tb_publicacao(tipo) VALUES (?) ''', self.tipo)

            conn.commit()
            id = cursor.lastrowid
            
            return id
        except:
            print("Ocorreu um ERRO!")
        finally:
            cursor.close()
            conn.close()

    def deletar(self, id_mens):
        try:

            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            cursor.execute(''' DELETE FROM tb_publicacao WHERE id =? ''', (id_mens))

            conn.commit()
        except:
            print("Ocorreu um ERRO!")
        finally:
            cursor.close()
            conn.close()

    def __str__(self):
        return "Publicação <%i>" %(self.id)
