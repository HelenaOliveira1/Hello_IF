'''
    Rede Social orientada à objeto
'''

class RedeSocial():
    def __init__(self, nome):
        self.nome = nome

    #Alterando o método __str__ de Rede Social
    def __str__(self):
        return "Rede Social <%s>"%(self.nome)

    #Alterando o método representativo de Amigo
    def __repr__(self):
        return self.__str__()
