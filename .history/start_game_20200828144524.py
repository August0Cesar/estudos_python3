import game_adivinhacao
import game_forca

print("########################################")
print("### Escolha o jogo! ####")
print("########################################")


print("(1) Forca (2) Adivinhacao")

game = input("Qual jogo? ")
if(game == 1):
    print("Abrindo jogo Forca")
elif(game == 2):
    print("Abrindo jogo Adivinhacao")