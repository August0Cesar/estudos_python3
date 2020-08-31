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


if(__name__ =="__main__"):
    jogar()
