from random import *

sorteio_pc = (randint(0,2))

jogada = int(input("Digite sua jogada (0=pedra, 1=papel, 2=tesoura): "))

if jogada <0 or jogada >2:
    print("Jogada Inválida")
    print(f"Computador jogou {sorteio_pc}")
    print(f"Jogador jogou {jogada}")
else:
    print(f"Computador jogou {sorteio_pc}")
    print(f"Jogador jogou {jogada}")

    if sorteio_pc == 0:
        if jogada == 0:
            print("Nenhum ganhador!")
        else:
            if jogada == 1:
                print("Você venceu :)")
            else:
                if jogada == 2:
                    print("Você perdeu :(")
    else:
        if sorteio_pc == 1:
            if jogada == 0:
                print("Você perdeu :(")
            else:
                if jogada == 1:
                    print("Nenhum ganhador!")
                else:
                    if jogada == 2:
                        print("Você venceu :)")
        else:
            if sorteio_pc == 2:
                if jogada == 0:
                    print("Você venceu :) ")
                else:
                    if jogada == 1:
                        print("Você perdeu :(")
                    else:
                        if jogada == 2:
                            print("Nenhum ganhador!")