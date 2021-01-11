class DescontoTotalItensMaiorCinco(object):
    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.value * 0.1
        else: 
            return self.__proximo_desconto.calcula(orcamento)


class DescontoValorMaiorQuinhentos(object):
    
    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        if orcamento.value > 500:
            return orcamento.value * 0.07
        else:
            return self.__proximo_desconto.calcula(orcamento)


class NenhumDesconto(object):
    def calcula(self, orcamento):
        return 0
