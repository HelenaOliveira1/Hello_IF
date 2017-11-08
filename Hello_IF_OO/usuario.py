"""
    Usuario Orientado a Objeto
"""

import sqlite3

conn = sqlite3.connect("hello_if.db")
cursor = conn.cursor()

class Usuario():

    def __init__(self, id, senha, login, logado, nome, data_nasc, genero, profissao):
        self.id = id
        self.senha = senha
        self.login = login
        self.logado = logado
        self.nome = nome
        self.data_nasc = data_nasc
        self.genero = genero
        self.profissao = profissao

    def listar(self):
        usuarios = []

        conn = sqlite3.connect("hello_if.db")
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM tb_usuario;
        ''')
        for linha in cursor.fechall():
            senha = linha[1]
            login = linha[2]
            logado = linha[3]
            nome = linha[4]
            data_nasc = linha[5]
            genero = linha[6]
            profissao = linha[7]
            usuario = Usuario(senha, login, logado, nome, data_nasc, genero, profissao)
            usuarios.append(usuario)

        conn.close()

        return usuarios

    def inserir(self):
        conn = sqlite3.connect("hello_if.db")
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO tb_usuario(senha, login, logado, nome, data_nasc, genero, profissao) VALUES (self.senha, self.login, self.logado,self.nome,self.data_nasc,self.genero,self.profissao)
        ''')

        conn.commit()
        conn.close()

    def deletar(self):
        pass

    def atualizar(self):
        pass

    def realizarBusca(self):
        pass

    def postPubPrivada(self):
        pass

    def postPubPublica(self):
        pass

    def enviarDM(self):
        pass

    def desfazerAmizade(self):
        pass

    def fazerAmigo(self):
        pass

    def comemorarTempoAmizade(self):
        pass