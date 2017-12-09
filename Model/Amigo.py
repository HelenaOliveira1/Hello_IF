"""
    Amigo Orientado a Objeto
"""

from Model.Usuario import *
import mysql
from database.Config_DB import *

class Amigo():

    def __init__(self, id, id_u, senha_u, login_u, logado_u, nome_u, data_nasc_u, genero_u, profissao_u, id_a, senha_a, login_a, logado_a, nome_a, data_nasc_a, genero_a, profissao_a):
        self.id = id
        self.usuario = Usuario(id_u, senha_u, login_u, logado_u, nome_u, data_nasc_u, genero_u, profissao_u)
        self.amigo = Usuario(id_a, senha_a, login_a, logado_a, nome_a, data_nasc_a, genero_a, profissao_a)

    def __str__(self):
        return "Amigo <%s>" %(self.nome)

    def __repr__(self):
        return self.__str__()
