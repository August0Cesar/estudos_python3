class Conta:

    def __init__(self, nome, numero, tipo, limite, saldo):
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite
        self.__nome = nome
        self.__tipo = tipo

    def extrato(self):
        return self.__saldo
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        if(self.__tem_saldo_suficiente(valor)):
            self.__saldo -= valor
        else:
            print("Não possui saldo suficiente para este saque")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

#Metodo private
    def __tem_saldo_suficiente(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel        


#Metodos acessores
    def get_saldo(self):
        return self.__saldo
    
    def get_numero(self):
        return self.__numero

    def get_nome(self):
        return self.__nome        

    #Getter e Setter
    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo
    
    #Getter e Setter usando @property
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    #Metodo statico
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB":"001", "CAIXA": "014", "BRADESCO":"276"}