'''
    Menu principal da rede social
'''

import sqlite3
from random import randint
import datetime
from Model.Usuario import Usuario
from Model.Amigo import Amigo
from database.RedeSocialDAO import RedeSocialDAO
from Model.RedeSocial import RedeSocial

'''
    Função para exibir o menu da Rede Social
'''
def exibirMenuPrincipal():

    print("==========  MENU  ==========\n"
        "1 - Criar ou entrar na Rede Social\n"
        "2 - Criar usuário\n"
        "3 - Adicionar Amigo\n"
        "4 - Desfazer Amizade\n"
        "5 - Realizar Busca\n"
        "6 - Enviar Mensagem\n"
        "0 - Sair\n")

    try:
        opcao = int(input("Digite a opção: "))

        return opcao

    except ValueError:
        print("Opção inválida")

'''
    Função Principal da rede
'''
def main(Args = []):

    cont = True

    print("==========   Bem vindo a nossa Rede Social!   ==========\n")

    while(cont):

        #Exibindo Menu de Opções
        op = exibirMenuPrincipal()

        #Criação da Rede Social
        if (op == 1):

            nome = str(input("Digite o nome da sua rede social: "))
            redeSocial = RedeSocial(nome)

            RedeSocialDAO.criarRedeSocial(redeSocial)

        # Criação do Usuário
        elif (op == 2):
            # Tratado os possiveis erros, se acontecer.
            try:

                id = randint(0,10000000)
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
                usuario = Usuario(id, senha, login, logado, nome, data_nasc, genero, profissao)

                cursor.execute('''
                        INSERT INTO tb_usuario(senha, login, logado, nome, data_nasc, genero, profissao)
                        VALUES (?,?,?,?,?,?,?)
                                ''',(usuario.senha, usuario.login, usuario.logado, usuario.nome, usuario.data_nasc, usuario.genero, usuario.profissao))

                conn.commit()
                print("Criado com sucesso!")

            except:
                print("Ocorreu um ERRO!...tente novamente mais tarde.")

        #Adicionar Amigo
        elif (op == 3):
            try:
                nome = input("Digite nome do amigo: ")

                cursor.execute('''
                    SELECT * FROM tb_amigo
                    WHERE nome LIKE nome=?
                    ''', (nome))

                Amigo.inserir()

                # Salvando no Banco de Dados
                conn.commit()
                print("Amigo adicionado com sucesso!")

            except:
                print("Ocorreu um ERRO!...tente novamente mais tarde.")

        #Desfazer Amizade
        elif(op == 4):
            try:
                Usuario.desfazerAmizade()

            except:
                print("Ocorreu um ERRO!...tente novamente mais tarde.")

        #Realizar Busca no Banco
        elif (op == 5):
            try:
                nome = str(input("Digite o nome do amigo: "))
                Usuario.realizarBusca(nome)

            except:
                print("Ocorreu um ERRO!...tente novamente mais tarde.")

        #Enviando Mensagem Privada
        elif (op == 6):
            try:
                Usuario.enviarDM()

            except:
                print("Ocorreu um ERRO!...tente novamente mais tarde.")

        #Saindo da Aplicação
        elif (op == 0):
            print("Saindo...")
            cont = False
            conn.close()

        #Se a opção for inválida
        else:
            print("Opção inválida")

if (__name__== '__main__'):
    main()
