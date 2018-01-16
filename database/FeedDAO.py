"""
    DML da tabela feed
"""

import mysql.connector
from database.ConfigDB import *

class FeedDAO():
    def inserir(self):
        # Tratando os possiveis erros
        try:
            # Conectando com o Banco e definindo o cursor
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            
            visibMens = str(input("Digite tipo da publicação: "))
            # Inserindo dados na tabela Feed
            cursor.execute("""
                INSERT INTO tb_feed (visib_mens)
                VALUES (?,?,?) """, (visibMens))

            # Salvando...
            conn.commit()
            print("Um registro inserido com sucesso.")
            id = cursor.lastrowid
            return id

        except mysql.connector.Error as error:
            print(error)
            print("Ocorreu um ERRO!")
            return False
        
        # Finalizando as operações
        finally:
            cursor.close()
            conn.close()

    def listar(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            publicacoes = []

            # Selecionando tudo da tabela Feed
            cursor.execute(""" 
                SELECT * FROM tb_feed; """)
            # Imprimindo os resultados
            for linha in cursor.fechall():
                usuario = linha[1]
                mensagem = linha[2]
                lista_feed = Feed(usuario, mensagem)
                publicacoes.append(lista_feed)

            # Salvando...
            conn.commit()
            print("Listamos com sucesso.")

        except:
            print("Ocorreu um ERRO!")

        finally:
            cursor.close()
            conn.close()
            return publicacoes

    def alterar(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            
            novoTipo = str(input("Digite novo tipo da publicação: "))
            # Alterando dados da tabela Feed
            cursor.execute("""
                UPDATE tb_feed
                SET novoTipo=?
                WHERE visib_mens = ?
                """, (novoTipo))

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

    def deletar(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            
            tipoPublicacao = int(input("Digite o tipo da publicação para remover: "))
            # Deletando dados da tabela Feed
            cursor.execute("""
                DELETE FROM tb_feed
                SET tipoPubicacao = ?
                WHERE visib_mens = ?
                """, (tipoPublicacao))

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