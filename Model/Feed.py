"""
    Feed Orientado a Objeto
"""

from Model.Usuario import Usuario
from Model.Mensagem import Mensagem
from database.FeedDAO import FeedDAO

class Feed():

    def __init__(self, senha_u, login_u, logado_u, nome_u, data_nasc_u, genero_u, profissao_u, visibilidade, texto):
        self.usuario = Usuario(senha_u, login_u, logado_u, nome_u, data_nasc_u, genero_u, profissao_u)
        self.mensagem = Mensagem(visibilidade, texto)

    def listar(self):
        FeedDAO.listar()
        
    def inserir(self):
        FeedDAO.inserir()

    def deletar(self):
        FeedDAO.deletar()

    def atualizar(self, visib_mens):
        FeedDAO.alterar()

    #Alterando o método __str__ de Feed
    def __str__(self):
        return "Feed <%i>" %(self.id)
    
    #Alterando o método representativo de Feed
    def __repr__(self):
        return self.__str__()
