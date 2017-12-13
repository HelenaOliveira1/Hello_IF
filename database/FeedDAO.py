"""
    DML da tabela feed
"""

import mysql.connector
from database.ConfigDB import *

class FeedDAO():
    def inserir_dados_feed(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            visib_mens = str(input("Digite tipo da publicação: "))

            cursor.execute("""
            INSERT INTO tb_publicacao (visib_mens)
            VALUES (?,?,?) """, (visib_mens))

            # Salvando...
            conn.commit()
            print("Um registro inserido com sucesso.")

        except mysql.connector.Error as error:
            print(error)
            print("Ocorreu um ERRO!")
            return False

        finally:
            cursor.close()
            conn.close()

    def lendo_imprimindo_feed(self):

        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute(""" SELECT * FROM tb_feed; """)

            for linha in cursor.fetchall():
                print(linha)

            # Salvando...
            conn.commit()
            print("Lemos com sucesso.")

        except:
            print("Ocorreu um ERRO!")

        finally:
            cursor.close()
            conn.close()

    def alterar_dados_feed(self):

        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            novo_tipo = str(input("Digite novo tipo da publicação: "))

            cursor.execute("""
                UPDATE tb_feed
                SET novo_tipo=?
                WHERE visib_mens = ?
                """, (novo_tipo))

            # Salvando...
            conn.commit()
            print("Registro alterado com sucesso.")

        except mysql.connector.Error as error:
            print(error)
            print("Ocorreu um ERRO!")
            return False

        finally:
            cursor.close()
            conn.close()

    def deletar_dados_feed(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            tipo_publicacao = int(input("Digite o tipo da publicação para remover: "))
            cursor.execute("""
                DELETE FROM tb_publicacao
                WHERE visib_mens = ?
                """, (tipo_publicacao))

            # Salvando...
            conn.commit()
            print("Registro deletado com sucesso.")

        except mysql.connector.Error as error:
            print(error)
            print("Ocorreu um ERRO!")
            return False

        finally:
            cursor.close()
            conn.close()
