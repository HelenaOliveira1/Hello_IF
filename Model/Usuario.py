"""
    Usuario Orientado a Objeto
"""

import mysql.connector
from Model.Amigo import *
from database.ConfigDB import *
from Model.Pessoa import Pessoa

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

class Usuario(Pessoa):
    def __init__(self, senha, login, logado, nome, data_nasc, genero, profissao):
        super(Usuario, self).__init__(nome, genero)
        self.senha = senha
        self.login = login
        self.logado = logado
        self.nome = nome
        self.data_nasc = data_nasc
        self.genero = genero
        self.profissao = profissao

    def __str__(self):
        return "Usuario <%s>" % (self.nome)

    def __repr__(self):
        return self.__str__()

    def realizarBusca(self, nome):
        try:

            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            cursor.execute(''' SELECT * FROM tb_usuario WHERE nome LIKE '%?%' ''', (nome))

            for linha in cursor.fetchall():
                print("%s\n", linha)

            conn.commit()
        except:
            print("Ocorreu um ERRO!")
        finally:
            cursor.close()
            conn.close()

    def postPubPrivada(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            texto = str(input("Digite o texto para ser enviado: "))
            usuario = str(input("Digite o nome do destinatário da publicação: "))

            cursor.execute('''SELECT nome FROM tb_usuario WHERE nome=? ''', (usuario))

            #Enviando mensagem...
            cursor.execute(''' UPDATE tb_publicacao SET texto=? ''', (texto))

            print("Publicação enviada com sucesso.")

            conn.commit()
        except:
            print("Ocorreu um ERRO!")
        finally:
            cursor.close()
            conn.close()

    def postPubPublica(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            texto = str(input("Digite o texto para ser enviado: "))

            cursor.execute('''SELECT nome FROM tb_usuario''')

            #Enviando mensagem...
            cursor.execute(''' UPDATE tb_publicacao SET texto=? ''', (texto))

            print("Publicação enviada com sucesso.")

            conn.commit()
        except:
            print("Ocorreu um ERRO!")
        finally:
            cursor.close()
            conn.close()

    def enviarDM(self): #Envio de mensagem
        try:

            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            texto = str(input("Digite o texto para ser enviado: "))
            usuario = str(input("Digite o nome do destinatário da mensagem: "))

            cursor.execute('''SELECT nome FROM tb_usuario WHERE nome=? ''', (usuario))

            #Enviando mensagem...
            cursor.execute(''' UPDATE tb_mensagem SET texto=? ''', (texto))

            print("Mensagem enviada com sucesso.")

            conn.commit()
        except:
            print("Ocorreu um ERRO!")
        finally:
            cursor.close()
            conn.close()

    def desfazerAmizade(self):
        try:
            opcao = int(input("Digite 1 para deletar amigo pelo id ou 2 para deletar o amigo pelo nome: "))

            if (opcao == 1):

                id_delt = int(input("Digite o id do seu amigo: "))
                Amigo.deletar(id_delt)

            elif (opcao == 2):

                nome_amigo = str(input("Digite o nome do seu amigo que deseja desfazer amizade:"))

                conn = mysql.connector.connect(**config)
                cursor = conn.cursor()

                cursor.execute('''DELETE FROM tb_amigo WHERE nome =? ''', (nome_amigo))
            else:
                print("Opção não existente.")

            conn.commit()
        except:
            print("Ocorreu um ERRO!")
        finally:
            cursor.close()
            conn.close()

    def fazerAmigo(self):
        try:
            Amigo.inserir()
        except:
            print("Ocorreu um ERRO!")

    def comemorarTempoAmizade(self):
        pass
