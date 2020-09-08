import game_adivinhacao
import game_forca
from be import be
def iniciar():

    print("########################################")
    print("### Escolha o jogo! ####")
    print("########################################")


    print("(1) Forca (2) Adivinhacao (3) test")

    game = int(input("Qual jogo? "))
    if(game == 1):
        print("Abrindo jogo Forca")
        game_forca.jogar()
    elif(game == 2):
        print("Abrindo jogo Adivinhacao")
        game_adivinhacao.jogar()
    elif(game == 3):
        be.test()





if(__name__ == "__main__"):
    iniciar()