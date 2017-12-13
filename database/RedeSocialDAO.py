'''
    DML da Rede Social
'''

import mysql.connector
from Model.RedeSocial import RedeSocial
from database.Tabelas import *

class RedeSocialDAO():
    def criarRedeSocial(redesocial: RedeSocial):
        
        # Conectando com o Banco e definindo o cursor
        conn = mysql.connect('%s.db'%redesocial.nome)
        cursor = conn.cursor()

        # Tratado os possiveis erros, se acontecer.
        try:
            criarTabelas(redesocial)
            print("Sua rede social '%s' foi criada com sucesso!" %redesocial.nome)
        except:
            print("Conexão bem sucedida com a rede social %s\n" %redesocial.nome)
        # Finalizando as operações
        finally:
            cursor.close()
            conn.close()
