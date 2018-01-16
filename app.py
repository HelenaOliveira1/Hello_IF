'''
    Menu principal da rede social
'''

import datetime
from Model.Usuario import Usuario
from Model.RedeSocial import RedeSocial
from database.ConfigDB import *
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
        "7 - Postar publicação Pública\n"
        "8 - Postar publicação Privada\n"
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
            print("Ops! A quantidade de dígitos é maior que a esperada!")
        senha = input("Digite uma senha: ")
        if (len(senha) > 25):
            print("Ops! A quantidade de dígitos é maior que a esperada!")
        logado = False
        nome = str(input("Digite seu nome: "))
        if (len(nome) > 70):
            print("Ops! A quantidade de dígitos é maior que a esperada!")
        dia = int(input("Digite dia de nascimento: "))
        mes = int(input("Digite mes de nascimento: "))
        ano = int(input("Digite ano de nascimento: "))
        data_nasc = datetime.date(ano, mes, dia)
        genero = str(input("Digite seu genero: "))
        if (len(genero) > 10):
            print("Ops!  A quantidade de dígitos é maior que a esperada!")
        profissao = str(input("Digite sua profissao: "))
        if (len(profissao) > 20):
            print("Ops! A quantidade de dígitos é maior que a esperada!")

        usuario = Usuario(senha, login, logado, nome, data_nasc, genero, profissao)
        usuarioDAO = UsuarioDAO()
        usuarioDAO.inserir(usuario)
        print("Usuário Criado!")

    except:
        print("Ocorreu um ERRO!\n Tente novamente mais tarde.")
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
            Usuario.fazerAmizade()

        #Desfazer Amizade
        elif(op == 4):
            Usuario.desfazerAmizade()

        #Realizar Busca no Banco
        elif (op == 5):
            Usuario.realizarBusca()

        #Enviando Mensagem Privada
        elif (op == 6):
            Usuario.enviarDM()

        # Posta publicação pública
        elif (op == 7):
            Usuario.postPubPublica()

        # Posta publicação privada
        elif (op == 8):
            Usuario.postPubPrivada()

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