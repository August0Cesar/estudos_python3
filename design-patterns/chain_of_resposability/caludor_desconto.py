from desconto import DescontoTotalItensMaiorCinco, DescontoValorMaiorQuinhentos, NenhumDesconto


class CalculadorDescontos(object):

    def calcula(self, orcamento):

        desconto = DescontoTotalItensMaiorCinco(
            DescontoValorMaiorQuinhentos(NenhumDesconto())
        ).calcula(orcamento)
        return desconto


if __name__ == '__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.add_item(Item('Item A', 100.0))
    orcamento.add_item(Item('Item B', 50.0))
    orcamento.add_item(Item('Item C', 400.0))
    # print(orcamento.total_itens)

    calculador_de_descontos = CalculadorDescontos()
    desconto = calculador_de_descontos.calcula(orcamento)
    print(f'Desconto calculado : {desconto}')
