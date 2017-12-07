"""
    DML da tabela amigo
"""

import mysql
from database.Config_DB import *
from Model.Amigo import *

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

def inserir(self):
    try:
        conn = mysql.conncetor.connect(**config)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tb_amigo(id, id_usuario, id_usuario_amigo) VALUES (?,?,?)
        ''', (self.id, self.usuario.id_u, self.amigo.id_a))

        conn.commit()
        id = cursor.lastrowid
        cursor.close()
        conn.close()

        return id

    except mysql.Error:
        print("Ocorreu um ERRO!")
        return False

    cursor.close()
    conn.close()


def listar(self):
    amigos = []

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM tb_amigo;
    ''')
    for linha in cursor.fechall():
        usuario = linha[1]
        amigo = linha[2]
        lista_amigo = Amigo(usuario, amigo)
        amigos.append(lista_amigo)

    cursor.close()
    conn.close()

    return amigos

def deletar(self, id_delt):
    conn = mysql.conncetor.connect(**config)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM tb_amigo
        WHERE id =?
        ''', id_delt)

    conn.commit()
    conn.close()