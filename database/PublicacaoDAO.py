"""
    DML da tabela publicação
"""

import mysql.connector
from database.ConfigDB import *

class PublicacaoDAO():
    def inserir(self):
        # Tratando os possiveis erros
        try:
            # Conectando com o Banco e definindo o cursor
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            tipo = str(input("Digite tipo da publicação: "))

            # Inserindo na tabela publicação
            cursor.execute("""
                INSERT INTO tb_publicacao (tipo)
                VALUES (?,?,?) """, (tipo))

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
            # Selecionando tudo da tabela publicação
            cursor.execute("""
            SELECT * FROM tb_publicacao;
            """)
            # Imprimindo os resultados
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
            novoTipo = str(input("Digite novo tipo da publicação: "))
            # Alterando os dados da tabela Mensagem
            cursor.execute("""
                UPDATE tb_mensagem
                SET novoTipo=?
                WHERE tipo = ?
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
            tipoPublicacao = int(input("Digite o tipo da publicação para remover: "))
            # Deletando os dados da tabela Publicação
            cursor.execute("""
                DELETE FROM tb_publicacao
                WHERE tipo = ?
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
