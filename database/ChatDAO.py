"""
    DML da tabela chat
"""

import mysql.connector
from database.ConfigDB import *

class ChatDAO():
    def inserir(self):
        # Tratando os possiveis erros
        try:
            # Conectando com o Banco e definindo o cursor
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            
            visib_mens = str(input("Digite tipo da publicação: "))
            
            # Inserindo dados na tabela Chat
            cursor.execute("""
                INSERT INTO tb_chat (visib_mens) 
                VALUES (?,?,?) """, (visib_mens))

            # Salvando...
            conn.commit()
            print("Um registro inserido com sucesso.")

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
            # Selecionando tudo da tabela Chat 
            cursor.execute("""
            SELECT * FROM tb_chat;
            """)
            # Imprimindo o resultado
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

    def alterar(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            
            novoTipo = str(input("Digite novo tipo da publicação: "))
            
            # Atualizando dados da tabela Chat
            cursor.execute("""
                UPDATE tb_chat
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
            
            # Deletando dados da tabela Chat 
            cursor.execute("""
                DELETE FROM tb_chat
                SET tipoPublicacao = ?
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
