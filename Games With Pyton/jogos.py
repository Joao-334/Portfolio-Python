import advinhacao
import forca2


def escolher():
    print("*********************************")
    print("********* Escolha seu Jogo! *********")
    print("*********************************")

    print("(1) Forca (2) Advinhação")
    jogo = int(input(print("Qual jogo você quer jogar? ")))

    if jogo == 1:
        print("Jogando Forca")
        forca2.jogar_forca()
    else:
        print("Jogando Advinhação")
        advinhacao.jogar_advinhacao()


if __name__ == "__main__":
    escolher()
