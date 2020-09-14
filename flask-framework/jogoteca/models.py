class Jogo:
    def __init__(self, nome, categoria, console, id=None):
        self._id = id
        self._nome = nome
        self._categoria = categoria
        self._console =console
    
    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def categoria(self):
        return self._categoria

    @property
    def console(self):
        return self._console

    @id.setter
    def id(self,id):
        self._id = id        

class Usuario:
    def __init__(self, id, nome, senha):
        self._id = id
        self._nome = nome
        self._senha = senha
    
    @property
    def id(self):
        return self._id
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def senha(self):
        return self._senha