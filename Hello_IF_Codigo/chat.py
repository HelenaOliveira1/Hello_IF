"""
    DML da tabela chat
"""
import sqlite3

conn = sqlite3.connect('hello_if.db')

cursor = conn.cursor()

def inserir_dados_chat():
    try:
        visib_mens = str(input("Digite tipo da publicação: "))

        cursor.execute("""
        INSERT INTO tb_chat (visib_mens)
        VALUES (?,?,?) """, (visib_mens))

        # Salvando...
        conn.commit()
        print("Um registro inserido com sucesso.")

    except sqlite3.Error:
        print("Ocorreu um ERRO!")
        return False

def lendo_imprimindo_chat():
    cursor.execute("""
    SELECT * FROM tb_chat;
    """)

    for linha in cursor.fetchall():
        print(linha)

    # Salvando...
    conn.commit()
    print("Lemos com sucesso.")

def alterar_dados_chat():
    try:
        novo_tipo = str(input("Digite novo tipo da publicação: "))

        cursor.execute("""
            UPDATE tb_mensagem
            SET novo_tipo=?
            WHERE visib_mens = ?
            """, (novo_tipo))

        # Salvando...
        conn.commit()
        print("Registro alterado com sucesso.")

    except sqlite3.Error:
        print("Ocorreu um ERRO!")
        return False

def deletar_dados_chat():
    try:
        tipo_publicacao = int(input("Digite o tipo da publicação para remover: "))
        cursor.execute("""
            DELETE FROM tb_publicacao
            WHERE visib_mens = ?
            """, (tipo_publicacao))

        # Salvando...
        conn.commit()
        print("Registro deletado com sucesso.")

    except sqlite3.Error:
        print("Ocorreu um ERRO!")
        return False
