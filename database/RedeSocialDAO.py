'''
    DML da Rede Social
'''

import mysql.connector
from database.Tabelas import RedeSocial

class RedeSocialDAO():
    #Função para criar a rede social
    def criarRedeSocial(redesocial: RedeSocial):
        # Tratado os possiveis erros, se acontecer.
        try:
            # Conectando com o Banco e definindo o cursor
            conn = mysql.connector.connect('%s.db'%redesocial.nome)
            cursor = conn.cursor()

            RedeSocial.criarTabelas(redesocial)
            print("Sua rede social '%s' foi criada com sucesso!" %redesocial.nome)
        except:
            print("Conexão bem sucedida com a rede social %s\n" %redesocial.nome)
        # Finalizando as operações
        finally:
            cursor.close()
            conn.close()