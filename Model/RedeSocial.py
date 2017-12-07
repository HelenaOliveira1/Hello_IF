'''
    Rede Social orientada à objeto
'''

class RedeSocial():

    def __init__(self, , senha = None, login = None, logado = None, nome, data_nasc = None, genero, profissao):
        self.senha = senha
        self.login = login
        self.logado = logado
        self.nome = nome
        self.data_nasc = data_nasc
        self.genero = genero
        self.profissao = profissao

    def __str__(self):
        return "Rede Social <%s>"%(self.nome)
