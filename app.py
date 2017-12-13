'''
    Menu principal da rede social
'''

import datetime
from random import randint
from Model.Usuario import Usuario
from Model.RedeSocial import RedeSocial
from database.AmigoDAO import *
from database.RedeSocialDAO import RedeSocialDAO
from database.UsuarioDAO import UsuarioDAO

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
        "7 - Postar publicação Pública"
        "8 - Postar publicação Privada"
        "0 - Sair\n")

    try:
        opcao = int(input("Digite a opção: "))

        return opcao

    except ValueError:
        print("Opção inválida")
        
'''
    Função para criar Rede Social
'''
def criarRedeSocial():
    try:
        nome = str(input("Digite o nome da sua rede social: "))
        redeSocial = RedeSocial(nome)
    
        RedeSocialDAO.criarRedeSocial(redeSocial)
    except:
        print("Ocorreu um ERRO!...tente novamente mais tarde.")
'''
    Criação do Usuário
'''
def criarUsuario():

    # Tratado os possiveis erros, se acontecer.
    try:
        login = input("Digite seu login: ")
        if(len(login)> 50):
            print("Ops! Ocorreu um erro")
        senha = input("Digite uma senha: ")
        if (len(senha) > 25):
            print("Ops! Ocorreu um erro")
        logado = False
        nome = str(input("Digite seu nome: "))
        if (len(nome) > 70):
            print("Ops! Ocorreu um erro")
        dia = int(input("Digite dia de nascimento: "))
        mes = int(input("Digite mes de nascimento: "))
        ano = int(input("Digite ano de nascimento: "))
        data_nasc = datetime.date(ano, mes, dia)
        genero = str(input("Digite seu genero: "))
        if (len(genero) > 10):
            print("Ops! Ocorreu um erro")
        profissao = str(input("Digite sua profissao: "))
        if (len(profissao) > 20):
            print("Ops! Ocorreu um erro")
        usuario = Usuario(senha, login, logado, nome, data_nasc, genero, profissao)
        usuarioDAO = UsuarioDAO()
        usuarioDAO.inserir(usuario)

    except:
        print("Ocorreu um ERRO!...tente novamente mais tarde.")
'''
    Função Principal da rede
'''
def main(Args = []):

    cont = True

    print("==========   Bem vindo a nossa Rede Social!   ==========\n")

    while(cont):

        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        #Exibindo Menu de Opções
        op = exibirMenuPrincipal()

        #Criação da Rede Social
        if (op == 1):
            criarRedeSocial()

        # Criação do Usuário
        elif (op == 2):
            criarUsuario()

        #Adicionar Amigo
        elif (op == 3):
            try:
                nome = input("Digite nome do amigo: ")

                cursor.execute('''
                    SELECT * FROM tb_amigo
                    WHERE nome LIKE nome=?
                    ''', (nome))

                AmigoDAO.inserir()

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

        elif (op == 7):
            try:
                Usuario.postPubPublica()

            except:
                print("Ocorreu um ERRO!...tente novamente mais tarde.")

        elif (op == 8):
            try:
                Usuario.postPubPrivada()

            except:
                print("Ocorreu um ERRO!...tente novamente mais tarde.")

        #Saindo da Aplicação
        elif (op == 0):
            print("Saindo...")
            cont = False
            cursor.close()
            conn.close()

        #Se a opção for inválida
        else:
            print("Opção inválida")

if (__name__== '__main__'):
    main()
