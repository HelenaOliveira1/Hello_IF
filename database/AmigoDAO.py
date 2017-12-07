"""
    DML da tabela amigo
"""

import mysql
from database.Config_DB import *

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

def inserir_dados_amigo():

    # Tratado os possiveis erros, se acontecer.
    try:
        email_amigo = input("Digite o email do seu amigo: ")

        sql = ("""
            SELECT * FROM tb_amigo
            WHERE login LIKE login=?""",(email_amigo))

        cursor.execute(sql)
        cursor.execute("""
            SELECT * FROM tb_usuario WHERE login=?
        """, email_amigo)

        # Salvando...
        conn.commit()
        print("Sucesso.")

    except mysql.Error:
        print("Ocorreu um ERRO!")
        return False
    cursor.close()
    conn.close()

def lendo_imprimindo_todos_amigos():

    cursor.execute("""
    SELECT * FROM tb_amigos;
    """)

    for linha in cursor.fetchall():
        print(linha)

    # Salvando...
    conn.commit()
    print("Lemos com sucesso.")

    cursor.close()
    conn.close()

def alterar_dados_amigos():

       # Tratado os possiveis erros, se acontecer.
    try:
        # Salvando...
        conn.commit()
        print("Registro alterado com sucesso.")

    except mysql.Error:
        print("Ocorreu um ERRO!")
        return False

    cursor.close()
    conn.close()

def deletar_dados_amigos():

       # Tratado os possiveis erros, se acontecer.
    try:
        email_amigo = input("Digite o email do seu amigo: ")

        sql = ("""
            DELETE * FROM tb_amigo
            WHERE login LIKE login=?""",(email_amigo))

        cursor.execute(sql)

        # Salvando...
        conn.commit()
        print("Sucesso.")

    except mysql.Error:
        print("Ocorreu um ERRO!")
        return False

    cursor.close()
    conn.close()