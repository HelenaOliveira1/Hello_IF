"""
    DML da tabela mensagem
"""

import mysql.connector
from database.ConfigDB import *

class MensagemDAO():
    def inserir(self):
        # Tratando os possiveis erros
        try:
            # Conectando com o Banco e definindo o cursor
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            
            visibilidade = str(input("Digite visibilidade da mensagem: "))
            texto = str(input("Digite todo texto: "))
            assunto = str(input("Digite o assunto da mensagem: "))
            
            #Inserindo dados na tabela Mensagem
            cursor.execute("""
            INSERT INTO tb_mensagem (visibilidade, texto, assunto)
            VALUES (?,?,?) """, (visibilidade, texto, assunto))

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

            mensagens = []
            # Selecionando tudo da tabela Mensagem
            cursor.execute(""" 
                SELECT * FROM tb_mensagem; """)

            #Imprimindo os resultados
            for linha in cursor.fechall():
                visibilidade = linha[1]
                texto = linha[2]
                mensagem = Mensagem(visibilidade, texto)
                mensagens.append(mensagem)

            # Salvando...
            conn.commit()
            print("Lemos com sucesso.")

        except:
            print("Ocorru um ERRO!")

        finally:
            cursor.close()
            conn.close()
            return mensagens

    def alterar(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            
            novoVisibilidade = str(input("Digite nova visibilidade da mensagem: "))
            novoTexto = str(input("Digite novo texto: "))
            novoAssunto = str(input("Digite novo assunto da mensagem: "))
            #Alterando dados da tabela mensagem
            cursor.execute("""
                UPDATE tb_mensagem
                SET novoVisibilidade=?, novoTexto=?, novoAssunto=?
                WHERE login =?
                """, (novoVisibilidade, novoTexto, novoAssunto))

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
            
            assuntoMensagem = int(input("Digite o assunto da mensagem para remover: "))
            
            cursor.execute("""
                DELETE FROM tb_mensagem
                SET assuntoMensagem =?
                WHERE assunto =?
                """, (assuntoMensagem))

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