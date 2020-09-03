from abc import ABCMeta, abstractmethod

class Programa(metaclass = ABCMeta):
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._like = 0

    @abstractmethod 
    def __str__(self): 
        pass

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

    # def __str__(self):
    #     return f'{self._nome} - {self._ano} - {self._like}'    


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao
    
    def __str__(self):
        return f'{self._nome} - {self._ano} - {self.__duracao} - {self._like}'
    
    

    


class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.__temporada = temporada      
    
    def __str__(self):
        return f'{self._nome} - {self._ano} - {self.__temporada} - {self._like}'
    


class PlayList:
    def __init__(self, nome, lista_programas):
        self.nome = nome
        self._lista_programas = lista_programas
    
    def tamanho_lista(self):
        return len(self._lista_programas)

    # duck typing
    def __getitem__(self, item):
        return self._lista_programas[item]   
    
    def __len__(self):
        return len(self._lista_programas)



vingadores = Filme("vingadores - a era de ultron",2018, 180)
bad_boys = Filme("Bad Boys 2",2004, 120)
guerra_thronos = Serie("Games of thrones - 2° season", 2013, 3)
supernatural = Serie("Supernatural - 5° season", 2016, 15)

vingadores.add_like()
vingadores.add_like()

bad_boys.add_like()

guerra_thronos.add_like()
guerra_thronos.add_like()

supernatural.add_like()
supernatural.add_like()
supernatural.add_like()

guerra_thronos.add_like()

# print(guerra_thronos.nome)
# print(vingadores.nome)

lista_programas = [vingadores, guerra_thronos, bad_boys, supernatural]
minha_playlist = PlayList("minha playlist", lista_programas)

print(len(minha_playlist))

for programa in minha_playlist:
    # print(programa.__str__())
    print(str(programa))
    # print(repr(programa))