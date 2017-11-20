'''
    Menu principal da rede social
'''

def main(Args = []):
    import sqlite3
    from random import randint
    import datetime
    from Model.usuario import Usuario
    from Model.amigo import Amigo

    cont = False

    print("==========   Bem vindo a nossa Rede Social!   ==========\n")

    op  = ''

    while(True):
        try:
            op = int(input("==========  MENU  ==========\n 1 - Criar ou entrar na Rede Social\n 2 - Sair\n"))
            if (op != 1 and op != 2):
                print("Número inválido")
            else:
                break
        except ValueError:
            print("Opção inválida")


    if (op == 1):

        nome = str(input("Digite o nome da sua rede social: "))

        try:



            conn = sqlite3.connect('%s.db'%nome)
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
        except:
            print("Conexão bem sucedida com a rede social %s\n " %nome)



        op2 = int(input("==========  MENU  ==========\n1 - Criar usuário\n 2 - Adicionar Amigo\n 3 - Desfazer Amizade\n 4 - Realizar Busca\n 0 - Sair\n"))
        cond = True

        while (cond):
            while (op2 != 1 and op2 != 2 and op2 != 3 and op2 != 4 and op2 != 5 and op2 != 0):
                print("Opção não existe.")
                op2 = int(input("==========  MENU  ==========\n1 - Criar usuário\n 2 - Adicionar Amigo\n 3 - Sair\n"))

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
                        INSERT INTO tb_usuario(senha, login, logado, nome, data_nasc, genero, profissao) 
                        VALUES (?,?,?,?,?,?,?)
                                ''',(senha, login, logado, nome, data_nasc, genero, profissao))

                conn.commit()
                print("Criado com sucesso!")
                op2 = int(input("==========  MENU  ==========\n 1 - Criar usuário\n 2 - Adicionar Amigo\n 3 - Enviar mensagem\n 4 - Desfazer Amizade\n 5 - Realizar Busca\n 0 - Sair\n"))

            elif (op2 == 2):
    
                # Tratado os possiveis erros, se acontecer.
                try:
                    nome = input("Digite nome do amigo: ")
                    sql = ("""
                        SELECT * FROM tb_amigo
                        WHERE nome LIKE nome=?
                        """, (nome))

                    cursor.execute(sql)
                    
                    Amigo.inserir()

                    # Salvando no Banco de Dados
                    conn.commit()
                    print("Tudo certo nada errado... Até agora.")

                except sqlite3.Error:

                    print("Ocorreu um ERRO!...tente novamente mais tarde.")
                    return False
                    op2 = int(input("==========  MENU  ==========\n 1 - Criar usuário\n 2 - Adicionar Amigo\n 3 - Enviar mensagem\n 4 - Desfazer Amizade\n 5 - Realizar Busca\n 0 - Sair\n"))
                
            elif (op2 == 3):
                Usuario.enviarDM()

            elif (op2 == 4):
                Usuario.desfazerAmizade()

            elif (op2 == 5):
                nome = str(input("Digite o nome do amigo: "))
                Usuario.realizarBusca(nome)

            elif (op2 == 0):
                print("Saindo...\nOBS.: Todos os dados serão perdidos.")
                cond = False
                conn.close()

            else:
                print("Opção inválida")

    elif (op == 2):
        print("Saindo...")

if (__name__== '__main__'):
    main()
