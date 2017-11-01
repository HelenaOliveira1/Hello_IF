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

import sqlite3

conn = sqlite3.connect('hello_if.db')

cursor = conn.cursor()

def lendo_imprimindo_todos_amigos():
    cursor.execute("""
    SELECT * FROM tb_amigos;
    """)

    for linha in cursor.fetchall():
        print(linha)

    # Salvando...
    conn.commit()
    print("Lemos com sucesso.")

def alterar_dados_amigos():
    try:
        # Salvando...
        conn.commit()
        print("Registro alterado com sucesso.")

    except sqlite3.Error:
        print("Ocorreu um ERRO!")
        return False

def deletar_dados_amigos():
    try:
        login_usuario = int(input("Digite o login do usuario para remover: "))
        cursor.execute("""
            DELETE FROM tb_amigo
            WHERE id_usuario_amigo = ?
            """, (login_usuario))

        # Salvando...
        conn.commit()
        print("Registro deletado com sucesso.")

    except sqlite3.Error:
        print("Ocorreu um ERRO!")
        return False
