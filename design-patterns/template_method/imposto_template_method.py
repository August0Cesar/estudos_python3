from abc import ABCMeta, abstractmethod

class TemplateCalculaImpostoMaximoOrMinimo(metaclass=ABCMeta):

    def calcula(self, orcamento):

        if self.calcula_taxa_maxima(orcamento):
            return self.calcula_valor_taxa_maxima(orcamento)
        else:
            return self.calcula_valor_taxa_mainima(orcamento)

    @abstractmethod
    def calcula_taxa_maxima(self, orcamento):
        pass

    @abstractmethod
    def calcula_valor_taxa_maxima(self, orcamento):
        pass

    @abstractmethod
    def calcula_valor_taxa_mainima(self, orcamento):
        pass


class ImpostoICCP(TemplateCalculaImpostoMaximoOrMinimo):
    
    def calcula_taxa_maxima(self, orcamento):
        return orcamento.value > 500
    
    def calcula_valor_taxa_maxima(self, orcamento):
        return orcamento.value * 0.07

    def calcula_valor_taxa_mainima(self, orcamento):
        return orcamento.value * 0.07

class ImpostoIKCV(TemplateCalculaImpostoMaximoOrMinimo):
    
    def calcula_taxa_maxima(self, orcamento):
        return orcamento.value > 500 and self.__tem_item_maior_que_100_reais(orcamento)
    
    def calcula_valor_taxa_maxima(self,orcamento):
        return orcamento.value * 0.10

    def calcula_valor_taxa_mainima(self,orcamento):
        return orcamento.value * 0.06

    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if(item.value > 100):
                return True
        return False
