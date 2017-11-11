'''
    Menu principal da rede social
'''

def main(Args = []):
    import sqlite3
    from random import *
    import datetime
    from Model.usuario import Usuario

    print("Bem vindo a nossa Rede Social!")
    op = int(input("Menu:\n 1- Criar outra Rede Social\n 2- Sair\n:"))

    while (op != 1 and op != 2):
        print ("Opção não existe.")
        op = int(input("Menu:\n 1- Criar Rede Social\n 2- Sair\n:"))

    if (op == 1):

        nome = str(input("Digite o nome da sua rede social: "))
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE tb_usuario (
    	    id INTEGER PRIMARY KEY AUTOINCREMENT,
    	    senha VARCHAR(25) NOT NULL,
    	    login VARCHAR(50) NOT NULL,
    	    logado BOOLEAN,
    	    nome VARCHAR(70) NOT NULL,
    	    data_nasc DATE,
    	    genero VARCHAR(10),
    	    profissao VARCHAR(20));
    	    """)
        cursor.execute("""
        CREATE TABLE tb_amigo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
    	    id_usuario INTEGER NOT NULL,
    	    id_usuario_amigo INTEGER NOT NULL,
    	    foreign key (id_usuario) references tb_usuario(id),
    	    foreign key (id_usuario_amigo) references tb_usuario(id));
    	    """)

        conn.commit()

        print("Sua rede social '%s' foi criada com sucesso!" %nome)

        op2 = int(input("Menu:\n 1- Criar usuário\n 2- Adicionar Amigo\n 3- Sair\n:"))
        cond = True

        while (cond):
            while (op2 != 1 and op2 != 2 and op2 != 3):
                print("Opção não existe.")
                op2 = int(input("Menu:\n 1- Criar usuário\n 2- Adicionar Amigo\n 3- Sair\n:"))

            if (op2 == 1):

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
                Usuario(id, senha, login, logado, nome, data_nasc, genero, profissao)
                cursor.execute('''
                        INSERT INTO tb_usuario(senha, login, logado, nome, data_nasc, genero, profissao) VALUES (senha, login, logado,nome,data_nasc,genero,profissao)
                                ''')

                conn.commit()
                print("Criado com sucesso!")
                op2 = int(input("Menu:\n 1- Criar usuário\n 2- Adicionar Amigo\n 3- Sair\n:"))

            elif (op2 == 2):
                print("Adicionar Amigo")
                op2 = int(input("Menu:\n 1- Criar usuário\n 2- Adicionar Amigo\n 3- Sair\n:"))

            elif (op2 == 3):
                print("Saindo...\nOBS.: Todos os dados serão perdidos.")
                cond = False
                conn.close()

    elif (op == 2):
        print("Saindo...")
        conn.close()

if (__name__== '__main__'):
    main()