"""
    DML da tabela mensagem
"""

import mysql
from database.Config_DB import *

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

def inserir_dados_mensagem():
    try:
        visibilidade = str(input("Digite visibilidade da mensagem: "))
        texto = str(input("Digite todo texto: "))
        assunto = str(input("Digite o assunto da mensagem: "))

        cursor.execute("""
        INSERT INTO tb_mensagem (visibilidade, texto, assunto)
        VALUES (?,?,?) """, (visibilidade, texto, assunto))

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

def lendo_imprimindo_todas_mensagens():
    try:
        cursor.execute(""" SELECT * FROM tb_mensagem; """)

        for linha in cursor.fetchall():
            print(linha)

        # Salvando...
        conn.commit()
        print("Lemos com sucesso.")
    
    except:
        print("Ocorru um ERRO!")

    finally:
        cursor.close()
        conn.close()

def alterar_dados_mensagem():
    try:
        novo_visibilidade = str(input("Digite nova visibilidade da mensagem: "))
        novo_texto = str(input("Digite novo texto: "))
        novo_assunto = str(input("Digite novo assunto da mensagem: "))

        cursor.execute("""
            UPDATE tb_mensagem
            SET novo_visibilidade=?, novo_texto=?, novo_assunto=?
            WHERE login = ?
            """, (novo_visibilidade, novo_texto, novo_assunto))

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

def deletar_dados_mensagem():
    try:
        assunto_mensagem = int(input("Digite o assunto da mensagem para remover: "))
        cursor.execute("""
            DELETE FROM tb_mensagem
            WHERE assunto = ?
            """, (assunto_mensagem))

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
