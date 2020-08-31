def jogar():
    print("########################################")
    print("### Bem Vindo ao  Jogo de Forca ########")
    print("########################################")

    palavra_chave = "banana"
    acertou       = False
    inforcado     = False

    lista_palavras_certas = ["_","_","_","_","_","_"]
    print(lista_palavras_certas)
    while(not acertou and not inforcado):
        chute         = input("Digite uma letra ")
        chute = chute.strip().upper()
        index         = 0
        for letra in palavra_chave:
            if(chute.upper() == letra.upper()):
                # print("Letra {} encontrada na posicao {}".format(letra,index))
                lista_palavras_certas[index] = letra
            index += 1
            # print(letra)
        print(lista_palavras_certas)    

    print("Jogo Finalizado")


if(__name__ =="__main__"):
    jogar()
