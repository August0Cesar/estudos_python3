import random

qtd_tentativas = 3

val_secreto = random.randrange(0, 101)
print("Valor Secreto {}".format(val_secreto))

for tentativa in range(qtd_tentativas):
    print("-------- Tentativa {} de {}. -------- ".format((tentativa + 1),qtd_tentativas))

    val_chute = int(input("Digite um valor "))
    valor_menor = int(val_chute) < val_secreto
    valor_maior = int(val_chute) > val_secreto

    if(chute < 1 or chute > 100):
        print('Você deve digitar um valor entre 1 e 100')

    if(val_chute == val_chute):
        print("#### Você acertou miseraveu. ####")
        break
    elif (valor_menor):
        print("#### Você errou. O valor digitado é menor que o valor secreto. ####")
        continue
    elif (valor_maior):
        print("#### Você errou. O valor digitado é maior que o valor secreto. ####")
        continue

    
print("####################")    
print("Jogo Finalizado")
print("####################")    