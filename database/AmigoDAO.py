"""
    DML da tabela amigo
"""

import mysql.connector
from database.ConfigDB import config
from Model.Amigo import Amigo

class AmigoDAO():
    def inserir(self):
        # Tratando os possiveis erros
        try:
            # Conectando com o Banco e definindo o cursor
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            # Inserindo dados na tabela Amigo
            cursor.execute('''
                INSERT INTO tb_amigo(id, id_usuario, id_usuario_amigo) 
                VALUES (?,?,?)''', (self.id, self.usuario.id_u, self.amigo.id_a))
            
            # Salvando...
            conn.commit()
            id = cursor.lastrowid
            return id

        except mysql.connector.Error as error:
            print(error)
            print("Ocorreu um ERRO!")
            return False
        
        # Finalizando as operações
        finally:
            cursor.close()
            conn.close()

    def listar(self):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            amigos = []
            
            # Selecionando tudo da tabela Amigo
            cursor.execute('''
                SELECT * FROM tb_amigo;
            ''')
            
            # Imprimindo resultados
            for linha in cursor.fechall():
                usuario = linha[1]
                amigo = linha[2]
                listaAmigo = Amigo(usuario, amigo)
                amigos.append(listaAmigo)

            return amigos

        except:
            print("Ocorreu um ERRO!")

        finally:
            cursor.close()
            conn.close()

    def deletar(self, id_delt):
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            
            # Deletando através do id uma tupla da tabela Amigo
            cursor.execute('''
                DELETE FROM tb_amigo
                WHERE id =?
                ''', id_delt)
        except:
            print("Ocorreu um ERRO!")

        finally:
            conn.commit()
            conn.close()