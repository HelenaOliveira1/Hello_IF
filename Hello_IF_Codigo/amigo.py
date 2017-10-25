"""
    DML da tabela amigo
"""

import sqlite3

conn = sqlite3.connect('hello_if.db')

cursor = conn.cursor()

def inserir_dados_amigo():
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

    except sqlite3.Error:
        print("Ocorreu um ERRO!")
        return False


