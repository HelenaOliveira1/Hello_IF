"""
    Publicação Orientado a Objeto
"""

from database.PublicacaoDAO import PublicacaoDAO

class Publicacao():
    def __init__(self, tipo):
        self.tipo = tipo

    def listar(self):
        PublicacaoDAO.listar()

    def inserir(self):
        PublicacaoDAO.inserir()

    def deletar(self):
        PublicacaoDAO.deletar()

    def atualizar(self):
        PublicacaoDAO.alterar()

    #Alterando o método __str__ de Publicação
    def __str__(self):
        return "Publicação <%i>" %(self.id)

    #Alterando o método representativo de Amigo
    def __repr__(self):
        return self.__str__()
