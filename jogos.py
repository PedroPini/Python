import forca
import advinhacao

def escolhe_jogo():
    print(__name__)
    print("********************************")
    print("*******Escolha o seu jogo*******")
    print("********************************")

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual Jogo?"))

    if(jogo == 1):
        forca.jogar()
    elif(jogo == 2):
        advinhacao.jogar()
    else:
        print("Jogo não existente!")
if(__name__ == "__main__"):
    escolhe_jogo()