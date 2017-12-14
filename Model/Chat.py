"""
    Chat Orientado a Objeto
"""

from Model.Usuario import Usuario
from Model.Mensagem import Mensagem
from database.ChatDAO import ChatDAO

class Chat():
    #Inicializando o objeto Chat
    def __init__(self, senha_u, login_u, logado_u, nome_u, data_nasc_u, genero_u, profissao_u, senha_a,
                 login_a, logado_a, nome_a, data_nasc_a, genero_a, profissao_a, visibilidade, texto):
        self.usuario = Usuario(senha_u, login_u, logado_u, nome_u, data_nasc_u, genero_u, profissao_u)
        self.amigo = Usuario(senha_a, login_a, logado_a, nome_a, data_nasc_a, genero_a, profissao_a)
        self.mensagem = Mensagem(visibilidade, texto)

    #Função para listar o Chat
    def listar(self):
        ChatDAO.listar()

    def inserir(self):
        ChatDAO.inserir()

    def deletar(self):
        ChatDAO.deletar()

    def alterar(self):
        ChatDAO.alterar()

    #Alterando o método __str__ de Chat
    def __str__(self):
        return "Chat <%i>" %(self.id)

    #Alterando o método representativo de Chat
    def __repr__(self):
        return self.__str__()
