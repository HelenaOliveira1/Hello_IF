"""
    Mensagem Orientado a Objeto
"""

from database.MensagemDAO import MensagemDAO

class Mensagem():

    def __init__(self, visibilidade, texto):
        self.visibilidade = visibilidade
        self.texto = texto

    def listar(self):
        MensagemDAO.listar()

    def inserir(self):
        MensagemDAO.inserir()
        
    def deletar(self):
        MensagemDAO.deletar()
    
    def atualizar(self):
        MensagemDAO.alterar()
        
    #Alterando o método __str__ de Mensagem
    def __str__(self):
        return "Mensagem <%i>" %(self.id)
    
    #Alterando o método representativo de Mensagem
    def __repr__(self):
        return self.__str__()
