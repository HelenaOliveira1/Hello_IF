"""
    App.py conecta o banco e cria todas as tabelas de Hello_IF
"""

import sqlite3

# Conectando o Banco de dados
conn = sqlite3.connect('hello_if.db')

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
	id_usuario_amigo INTEGER NOT NULL);
	""")

print("Tabela tb_amigo criada com sucesso.")

cursor.execute("""
    CREATE TABLE tb_mensagem (
	visibilidade VARCHAR(10),
	texto TEXT,
	assunto TEXT);
	""")

print("Tabela tb_mensagem criada com sucesso.")

cursor.execute("""
    CREATE TABLE tb_feed (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_usuario INTEGER NOT NULL,
	visib_mens VARCHAR(10));
	""")

print("Tabela tb_feed criada com sucesso.")

cursor.execute("""
    CREATE TABLE tb_chat (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_usuario INTEGER NOT NULL,
	visib_mens VARCHAR(10),
	id_usuario_amigo INTEGER);
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
conn.close()
