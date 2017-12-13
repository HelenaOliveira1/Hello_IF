"""
    Criação das tabelas de Hello_IF
"""

import mysql.connector
from Model.RedeSocial import RedeSocial

class Rede_Social():
    def criarTabelas(redesocial: RedeSocial):
        # Conectando o Banco de dados
        conn = mysql.connector.connect("%s.db"%redesocial.nome)

        # Criando o cursor
        cursor = conn.cursor()

        # Criando todas as tabelas
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

        print("Tabela tb_usuario criada com sucesso.")

        cursor.execute("""
            CREATE TABLE tb_amigo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                id_usuario_amigo INTEGER NOT NULL,
                foreign key (id_usuario) references tb_usuario(id),
                foreign key (id_usuario_amigo) references tb_usuario(id));
            """)

        print("Tabela tb_amigo criada com sucesso.")

        cursor.execute("""
            CREATE TABLE tb_mensagem (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                visibilidade VARCHAR(10),
                texto TEXT,
                assunto TEXT);
            """)

        print("Tabela tb_mensagem criada com sucesso.")

        cursor.execute("""
            CREATE TABLE tb_feed (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                visib_mens VARCHAR(10),
                foreign key (id_usuario) references tb_usuario(id),
                foreign key (visib_mens) references tb_mensagem(visibilidade));
            """)

        print("Tabela tb_feed criada com sucesso.")

        cursor.execute("""
            CREATE TABLE tb_chat (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                visib_mens VARCHAR(10),
                id_usuario_amigo INTEGER,
                foreign key (id_usuario) references tb_usuario(id),
                foreign key (visib_mens) references tb_mensagem(visibilidade),
                foreign key (id_usuario_amigo) references tb_usuario(id));
            """)

        print("Tabela tb_chat criada com sucesso.")

        cursor.execute("""
            CREATE TABLE tb_publicacao (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo VARCHAR(10));
            """)

        print("Tabela tb_publicacao criada com sucesso.")

        # Salvando...
        conn.commit()

        # Desconectando...
        cursor.close()
        conn.close()
