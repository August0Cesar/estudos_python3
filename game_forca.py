import random

def jogar():
    print("########################################")
    print("### Bem Vindo ao  Jogo de Forca ########")
    print("########################################")

    arquivo = open("palavras.txt", "r")
    palavras = []
    # for palavra in arquivo:
    #     palavras.append(palavra.strip().upper())
    
    # arquivo.close()
    with open("palavras.txt", "r") as arquivo:
        for palavra in arquivo:
            palavras.append(palavra.strip().upper())





    index_palavra = random.randrange(0,len(palavras))
    palavra_chave = palavras[index_palavra]
    acertou       = False
    inforcado     = False
    tentativas    = 0

    #List Comprehensions ["_" for letra in palavra_chave]
    lista_palavras_certas = ["_" for letra in palavra_chave]#List Comprehensions

    print(lista_palavras_certas)
    while(not acertou and not inforcado):
        
        chute         = input("Digite uma letra ")
        chute         = chute.strip().upper()
        index         = 0

        if (chute in palavra_chave):
            for letra in palavra_chave:
                if(chute == letra):
                    # print("Letra {} encontrada na posicao {}".format(letra,index))
                    lista_palavras_certas[index] = letra
                index += 1
                # print(letra)
            print(lista_palavras_certas)    
        else:
            tentativas +=1
        inforcado = tentativas == 6
        acertou   = "_" not in lista_palavras_certas

    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você Perdeu!!")
    print("Jogo Finalizado")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if(__name__ =="__main__"):
    jogar()

