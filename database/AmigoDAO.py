"""
    DML da tabela amigo
"""

import mysql.connector
from database.ConfigDB import config
from Model.Amigo import *

class AmigoDAO():
    def inserir(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO tb_amigo(id, id_usuario, id_usuario_amigo) VALUES (?,?,?)
            ''', (self.id, self.usuario.id_u, self.amigo.id_a))

            conn.commit()
            id = cursor.lastrowid

            return id

        except mysql.connector.Error as error:
            print(error)
            print("Ocorreu um ERRO!")
            return False

        finally:
            cursor.close()
            conn.close()


    def listar(self):

        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
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

            return amigos

        except:
            print("Ocorreu um ERRO!")

        finally:
            cursor.close()
            conn.close()

    def deletar(self, id_delt):

        try:
            conn = mysql.conncetor.connect(**config)
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM tb_amigo
                WHERE id =?
                ''', id_delt)
        except:
            print("Ocorreu um ERRO!")

        finally:
            conn.commit()
            conn.close()
