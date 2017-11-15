"""
    Usuario Orientado a Objeto
"""

import sqlite3

conn = sqlite3.connect(':memory:')
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

        conn = sqlite3.connect(':memory:')
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
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO tb_usuario(senha, login, logado, nome, data_nasc, genero, profissao) VALUES (senha, login, logado,nome,data_nasc,genero,profissao)
        ''')

        conn.commit()
        id = cursor.lastrowid
        conn.close()
        
        return id

    def deletar(self, id_delt):
        
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        
        cursor.execute('''
            DELETE FROM tb_usuario
            WHERE id =?
        ''', id_delt)

        conn.commit()
        conn.close()

    def atualizar(self, nova_senha, novo_login, novo_logado, novo_nome, nova_data_nasc, novo_genero, nova_profissao):
        
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE tb_usuario
            SET nova_senha = ?, novo_login = ?, novo_logado = ?, novo_nome = ?, nova_data_nasc = ?, novo_genero = ?, nova_profissao = ?
            VALUES (?,?,?,?,?,?,?)
            WHERE id=?
        ''', (nova_senha, novo_login, novo_logado, novo_nome, nova_data_nasc, novo_genero, nova_profissao, self.id))

        conn.commit()
        conn.close()

    def realizarBusca(self, nome):
        
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM tb_usuario
            WHERE nome LIKE '%?%'
        ''', (nome))
        
        conn.commit()
        conn.close()
        
    def postPubPrivada(self):
        pass

    def postPubPublica(self):
        pass

    def enviarDM(self): #Envio de mensagem
        
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        
        texto = str(input("Digite o texto para ser enviado: "))
        usuario = str(input("Digite o nome do destinatário da mensagem: "))
        
        cursor.execute('''
            SELECT nome FROM tb_usuario
            WHERE nome=?
        ''', (usuario))
        
        #Enviando mensagem...
        cursor.execute('''
           UPDATE tb_mensagem
           SET texto=?
        ''', (texto))
        
        print("Mensagem enviada com sucesso.")
        
        conn.commit()
        conn.close()
        
    def desfazerAmizade(self):

    nome_amigo = str(input("Digite o nome do seu amigo que deseja desfazer amizade:"))
    
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    cursor.execute('''
            DELETE FROM tb_amigo
            WHERE nome =?
        ''', (nome_amigo))

        conn.commit()
        conn.close()

    def fazerAmigo(self):
        pass

    def comemorarTempoAmizade(self):
        pass 
