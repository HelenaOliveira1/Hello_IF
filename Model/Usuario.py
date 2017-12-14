"""
    Usuario Orientado a Objeto
"""

from Model.Amigo import Amigo
from Model.Pessoa import Pessoa
from database.UsuarioDAO import UsuarioDAO

class Usuario(Pessoa):
    def __init__(self, senha, login, logado, nome, data_nasc, genero, profissao):
        super(Usuario, self).__init__(nome, data_nasc, genero, profissao)
        self.senha = senha
        self.login = login
        self.logado = logado

    def realizarBusca(self):
        
        nome = str(input("Digite o nome do seu amigo: "))
        UsuarioDAO.realizarBusca(nome)
        
    def postPubPrivada(self):
        UsuarioDAO.postPubPrivada()

    def postPubPublica(self):
        UsuarioDAO.postPubPublica()
        
    def enviarDM(self): #Envio de mensagem
        UsuarioDAO.enviarDM()

    def desfazerAmizade(self):
        UsuarioDAO.desfazerAmizade()

    def fazerAmizade(self):
        UsuarioDAO.fazerAmizade()

    def comemorarTempoAmizade(self):
        pass
    
    #Alterando o método __str__ de Usuário
    def __str__(self):
        return "Usuario <%s>" % (self.nome)
    
    #Alterando o método representativo de Amigo
    def __repr__(self):
        return self.__str__()
