class ImpostoICMS(object):
    
    def calcula(self, orcamento):
        return orcamento.value * 0.15

class ImpostoIRRS(object):
    
    def calcula(self,orcamento):
        return orcamento.value * 0.08
