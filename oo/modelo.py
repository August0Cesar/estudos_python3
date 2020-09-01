class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._like = 0

    def add_like(self):
        self._like += 1

    @property
    def like(self):
        return self._like


    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome    


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao
        

    


class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.__temporada = temporada      
    
    


vingadores = Filme("vingadores - a era de ultron",2018, 180)

guerra_thronos = Serie("Games of thrones - 2° season", 2013, 3)

print(guerra_thronos.nome)
print(vingadores.nome)