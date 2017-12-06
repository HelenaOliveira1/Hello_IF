'''
    DML da Rede Social
'''

import sqlite3
from Model.RedeSocial import RedeSocial
from database.Tabelas import *

class RedeSocialDAO():

    def criarRedeSocial(redesocial: RedeSocial):

        conn = sqlite3.connect('%s.db'%redesocial.nome)
        cursor = conn.cursor()

        # Tratado os possiveis erros, se acontecer.
        try:
            criarTabelas(redesocial)
            print("Sua rede social '%s' foi criada com sucesso!" %redesocial.nome)
        except:
            print("Conexão bem sucedida com a rede social %s\n " %redesocial.nome)
