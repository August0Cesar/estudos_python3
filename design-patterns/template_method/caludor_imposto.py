from imposto_template_method import ImpostoICCP, ImpostoIKCV
from imposto_strateggy import ImpostoICMS, ImpostoIRRS


class CalculadorImposto(object):

    def calcula(self, orcamento, imposto):

        imposto = imposto.calcula(orcamento)
        return imposto


if __name__ == '__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.add_item(Item('Item A', 100.0))
    orcamento.add_item(Item('Item B', 50.0))
    orcamento.add_item(Item('Item C', 400.0))


    calculador_de_imposto = CalculadorImposto()
    imposto = calculador_de_imposto.calcula(orcamento, ImpostoIKCV())
    print(f'Valor imposto IKCV calculado : {imposto}')
    imposto = calculador_de_imposto.calcula(orcamento, ImpostoICCP())
    print(f'Valor imposto ICCP calculado : {imposto}')
    imposto = calculador_de_imposto.calcula(orcamento, ImpostoICMS())
    print(f'Valor imposto ICMS calculado : {imposto}')
    imposto = calculador_de_imposto.calcula(orcamento, ImpostoIRRS())
    print(f'Valor imposto IRRS calculado : {imposto}')
