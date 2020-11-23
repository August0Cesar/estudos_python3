from desconto import DesontoTotalItensMaiorCinco, DesontoValorMaiorQuinhentos

class Calculador_de_descontos(object):

    def calcula(self, orcamento):

        desconto = DesontoTotalItensMaiorCinco().calcula(orcamento)
        if desconto == 0:
            desconto = DesontoValorMaiorQuinhentos().calcula(orcamento)
            return desconto


if __name__ == '__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.add_item(Item('Item A', 100.0))
    orcamento.add_item(Item('Item B', 50.0))
    orcamento.add_item(Item('Item C', 400.0))
    # print(orcamento.total_itens)

    calculador_de_descontos = Calculador_de_descontos()
    desconto = calculador_de_descontos.calcula(orcamento)
    print(f'Desconto calculado : {desconto}')
    # imprime 38.5      