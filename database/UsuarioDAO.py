"""
    DML da tabela usuario
"""

import mysql.connector
from Model.Usuario import Usuario
from database.ConfigDB import *
import datetime

class UsuarioDAO():
    def inserir(self, usuario):
        # Tratando os possiveis erros
        try:
            # Conectando com o Banco e definindo o cursor
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            # Inserindo na tabela os dados do usuario
            cursor.execute("""
                INSERT INTO tb_usuario (senha, login, logado, nome, data_nasc, genero, profissao)
                VALUES (?,?,?,?,?,?,?) """, 
                (usuario.senha, usuario.login, usuario.logado, usuario.nome, usuario.data_nasc, usuario.genero, usuario.profissao))

            # Salvando...
            conn.commit()
            print("Um registro inserido com sucesso.")

        except mysql.connector.Error as error:
            print(error)
            print("Ocorreu um ERRO!")
            return False
        # Finalizando as operações
        finally:
            conn.commit()
            id = cursor.lastrowid
            cursor.close()
            conn.close()
            return id

    def inserir(self):
        # Tratando os possiveis erros
        try:
            # Conectando com o Banco e definindo o cursor
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            
            lista = input("Digite uma lista tipo:[()]: ")
            # 
            cursor.executemany("""INSERT INTO tb_usuario (senha, login, logado, nome, data_nasc, genero, profissao)
            VALUES (?,?,?,?,?,?,?) """, lista)

            # Salvando...
            conn.commit()
            print("Registros inseridos com sucesso.")

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
            
            usuarios = []
            # selecionando tudo da tabela usuario 
            cursor.execute('''SELECT * FROM tb_usuario; ''')
            # 
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

    def alterar(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            
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
            
            # Alterando os dados do usuário
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

    def deletar(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            
            login_usuario = int(input("Digite o login do usuario para remover: "))
            # Deletando od dados da tabela usuario
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
