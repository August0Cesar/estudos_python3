class DesontoTotalItensMaiorCinco(object):

    def calcula(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.value * 0.1
        else: 
        # se não segue a regra, o desconto é zero!
            return 0


class DesontoValorMaiorQuinhentos(object):

    def calcula(self, orcamento):
        if orcamento.value > 500:
            return orcamento.value * 0.07
        else:
        # se não segue a regra, o desconto é zero
            return 0