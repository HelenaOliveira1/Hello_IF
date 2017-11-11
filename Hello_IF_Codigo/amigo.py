"""
    DML da tabela amigo
"""

import sqlite3

conn = sqlite3.connect('hello_if.db')
cursor = conn.cursor()

def ADDamigo():
    
        # Tratado os possiveis erros, se acontecer.
    try:
        nome = input("Digite seu nome completo: ")
        sql = ('''
            INSERT INTO tb_amigo
                VALUES amigo''', (nome))

        cursor.execute(sql)

        # Salvando no Banco de Dados
        conn.commit()
        print("Tudo certo nada errado... Até agora.")

    except sqlite3.Error:
        print("Ocorreu um ERRO!...ligue novamente mais tarde.")
        return False

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

    except sqlite3.Error:
        print("Ocorreu um ERRO!")
        return False

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
    
       # Tratado os possiveis erros, se acontecer.
    try:
        # Salvando...
        conn.commit()
        print("Registro alterado com sucesso.")

    except sqlite3.Error:
        print("Ocorreu um ERRO!")
        return False

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

    except sqlite3.Error:
        print("Ocorreu um ERRO!")
        return False
