from conta import Conta




conta1 = Conta("Augusto", 122, "Conta Corrente", 1000.0, 50.00)
conta2 = Conta("Augusto", 544, "Conta Corrente", 1000.0, 300.00)
print("Saldo Atual ------------------")
print(conta1.extrato())
print(conta2.extrato())

conta2.transferir(55, conta1)

print("Novo Atual ------------------")
print(conta1.extrato())
print(conta2.extrato())




print("usando metodos acessores")
print("Chamando get_nome -> {}".format(conta1.get_nome()))
print("Chamando get_tipo -> {}".format(conta1.get_tipo()))

print("Chamando set_tipo")
conta1.set_tipo("Poupanca")
print("Chamando get_tipo -> {}".format(conta1.get_tipo()))

print("Chamando limite -> {}".format(conta1.limite))
print("Settando valor para limite")
conta1.limite = 2000
print("Chamando limite -> {}".format(conta1.limite))


print("Chamando metodos estaticos")
print("Conta do banco da classe {}".format(Conta.codigo_banco()))
print("Contas de bancos {}".format(Conta.codigos_bancos()))


print("Saque saldo insuficiente")
conta1.sacar(10000)