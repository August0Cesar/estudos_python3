import random

def jogar():
    mensagemBoaVindas()

    palavras = inicializaPalavras()

    palavra_chave = seleciona_palavra_secreta(palavras)
    print(palavra_chave)
    
    acertou       = False
    inforcado     = False
    tentativas    = 0

    #List Comprehensions ["_" for letra in palavra_chave]
    lista_palavras_acertadas = ["_" for letra in palavra_chave]

    print(lista_palavras_acertadas)
    while(not acertou and not inforcado):
        
        chute = input("Digite uma letra ").strip().upper()
        
        if (chute in palavra_chave):
            mostra_palavras_acertadas(chute, lista_palavras_acertadas, palavra_chave)  
        else:
            tentativas +=1
            desenha_forca(tentativas)
            
        inforcado = tentativas == 7
        acertou   = "_" not in lista_palavras_acertadas

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_chave)

def seleciona_palavra_secreta(palavras):
    index_palavra = random.randrange(0,len(palavras))
    return palavras[index_palavra]

def mensagemBoaVindas():
    print("########################################")
    print("### Bem Vindo ao  Jogo de Forca ########")
    print("########################################")

def inicializaPalavras(file = "palavras.txt"):
    arquivo = open(file, "r")
    palavras = []
    # for palavra in arquivo:
    #     palavras.append(palavra.strip().upper())
    
    # arquivo.close()
    with open("palavras.txt", "r") as arquivo:
        for palavra in arquivo:
            palavras.append(palavra.strip().upper())
    return palavras

def mostra_palavras_acertadas(chute, lista_palavras_certas, palavra_chave):
    index = 0
    for letra in palavra_chave:
        if(chute == letra):
            # print("Letra {} encontrada na posicao {}".format(letra,index))
            lista_palavras_certas[index] = letra
        index += 1 
    print(lista_palavras_certas)

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
    # main()
    jogar()

