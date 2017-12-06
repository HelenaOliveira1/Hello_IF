'''
    Rede Social orientada à objeto
'''

class RedeSocial():

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "Rede Social <%s>"%(self.nome)
