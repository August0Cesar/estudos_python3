import random
#Funções built-in exemplo: abs

def jogar():
    print("########################################")
    print("### Bem Vindo ao Jogo de Advinhação ####")
    print("########################################")


    qtd_tentativas = 3
    pontos         = 1000
    val_secreto    = random.randrange(0, 101)

    print("Valor Secreto {}".format(val_secreto))

    for tentativa in range(qtd_tentativas):
        print("-------- Tentativa {} de {}. -------- ".format((tentativa + 1),qtd_tentativas))

        val_chute   = int(input("Digite um valor "))
        valor_menor = int(val_chute) < val_secreto
        valor_maior = int(val_chute) > val_secreto

        if(val_chute < 1 or val_chute > 100):
            print('Você deve digitar um valor entre 1 e 100')
            continue

        if(val_chute == val_secreto):
            print("#### Você acertou miseraveu. Você marcou {} potnos ####".format(pontos))
            break
        elif (valor_menor):
            print("#### Você errou. O valor digitado é menor que o valor secreto. ####")
            
        elif (valor_maior):
            print("#### Você errou. O valor digitado é maior que o valor secreto. ####")
            
        pontos_perdidos = abs(val_secreto - val_chute)
        pontos = pontos - pontos_perdidos

    
    print("Jogo Finalizado")

