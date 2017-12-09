"""
    DML da tabela usuario
"""

import mysql
from Model.Usuario import Usuario
from database.Config_DB import *
import datetime

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

def inserir_dados_usuario():
    try:
        login = input("Digite seu login: ")
        senha = input("Digite uma senha: ")
        logado = False
        nome = str(input("Digite seu nome: "))
        dia = int(input("Digite dia de nascimento: "))
        mes = int(input("Digite mes de nascimento: "))
        ano = int(input("Digite ano de nascimento: "))
        data_nasc = datetime.date(ano, mes, dia)
        genero = str(input("Digite seu genero: "))
        profissao = str(input("Digite sua profissao: "))

        cursor.execute("""
        INSERT INTO tb_usuario (senha, login, logado, nome, data_nasc, genero, profissao)
        VALUES (?,?,?,?,?,?,?) """, (senha, login, logado, nome, data_nasc, genero, profissao))

        # Salvando...
        conn.commit()
        print("Um registro inserido com sucesso.")

    except mysql.connector.Error as error:
        print(error)
        print("Ocorreu um ERRO!")
        return False

    finally:
        conn.commit()
        id = cursor.lastrowid
        cursor.close()
        conn.close()
        return id

def inserir_lista_usuario():

    try:
        lista = input("Digite uma lista tipo:[()]: ")
        cursor.executemany("""INSERT INTO tb_usuario (senha, login, logado, nome, data_nasc, genero, profissao)
        VALUES (?,?,?,?,?,?,?) """, lista)

        # Salvando...
        conn.commit()
        print("Registros inseridos com sucesso.")


    except mysql.connector.Error as error:
        print(error)
        print("Ocorreu um ERRO!")
        return False

    finally:
        cursor.close()
        conn.close()

def listar(self):
    try:
        usuarios = []

        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM tb_usuario; ''')
        for linha in cursor.fechall():
            senha = linha[1]
            login = linha[2]
            logado = linha[3]
            nome = linha[4]
            data_nasc = linha[5]
            genero = linha[6]
            profissao = linha[7]
            usuario = Usuario(senha, login, logado, nome, data_nasc, genero, profissao)
            usuarios.append(usuario)
        return usuarios

    except:
        print("Ocorreu um ERRO!")

    finally:
        cursor.close()
        conn.close()

def alterar_dados_usuario():
    try:
        novo_nome = str(input("Digite novo nome: "))
        novo_login = input("Digite novo login: ")
        novo_senha = input("Digite nova senha: ")
        novo_logado = False
        novo_dia = int(input("Digite novo dia de nascimento: "))
        novo_mes = int(input("Digite novo mes de nascimento: "))
        novo_ano = int(input("Digite novo ano de nascimento: "))
        novo_data_nasc = datetime.date(novo_ano, novo_mes, novo_dia)
        novo_genero = str(input("Digite novo genero: "))
        novo_profissao = str(input("Digite nova profissao: "))
        login_usuario = int(input("Digite o email do usuario para alterar: "))

        cursor.execute("""
            UPDATE tb_usuario
            SET novo_nome=?, novo_login=?, novo_senha=?,novo_logado=?,novo_data_nasc=?,novo_genero=?,novo_profissao=?
            WHERE login = ?
            """, (novo_nome, novo_login, novo_senha,novo_logado,novo_data_nasc,novo_genero,novo_profissao, login_usuario))

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

def deletar_dados_usuario():
    try:
        login_usuario = int(input("Digite o login do usuario para remover: "))
        cursor.execute(""" DELETE FROM tb_usuario WHERE login = ? """, (login_usuario))

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
