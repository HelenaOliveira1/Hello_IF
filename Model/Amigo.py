"""
    Amigo Orientado a Objeto
"""

from Model.Usuario import Usuario

class Amigo():
    #Inicializando o objeto Amigo
    def __init__(self, id, senha_u, login_u, logado_u, nome_u, data_nasc_u, genero_u, profissao_u, senha_a, login_a, logado_a, nome_a, data_nasc_a, genero_a, profissao_a):
        self.id = id
        self.usuario = Usuario(senha_u, login_u, logado_u, nome_u, data_nasc_u, genero_u, profissao_u)
        self.amigo = Usuario(senha_a, login_a, logado_a, nome_a, data_nasc_a, genero_a, profissao_a)
    #Alterando o método __str__ de Amigo
    def __str__(self):
        return "Amigo <%s>" %(self.nome)
    #Alterando o método representativo de Amigo
    def __repr__(self):
        return self.__str__()
