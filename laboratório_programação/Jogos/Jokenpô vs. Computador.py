#Desenvolva o clássico jogo onde o usuário escolhe entre Pedra, Papel ou Tesoura.
#O computador fará a sua escolha aleatoriamente. O sistema então determina e exibe 
#o vencedor da rodada (usuário, computador ou empate) e,
#opcionalmente, mantém um placar

import random

def jokenpô():
    compu = random.randint(1,3)
    tentativa = 0
    fim=0
    print("Jokenpô. 1 = Pedra, 2 = Papel, 3 = Tesoura.\n")

    tentativa = int(input("Digite seu palpite: "))
    while fim==0:
        #derrotas
        if tentativa == 1 and compu == 2:
            print("Sua Pedra foi embrulhada, você perdeu.")
            fim=1
        elif tentativa == 2 and compu == 3:
            print("Seu Papel foi cortado, você perdeu.")
            fim=1
        elif tentativa == 3 and compu == 1:
            print("Sua Tesoura foi quebrada, você perdeu.")
            fim=1
        elif tentativa !=1 and tentativa !=2 and tentativa !=3:
            print("Você não jogou a sua mão e perdeu.")
            fim=1
    
        #vitórias
        elif tentativa == 2 and compu == 1:
            print("Seu Papel embrulhou a Pedra, você venceu.")
            fim=1
        elif tentativa == 3 and compu == 2:
            print("Sua Tesoura cortou o Papel, você venceu.")
            fim=1
        elif tentativa == 1 and compu == 3:
            print("Sua Pedra quebrou a Tesoura, você venceu.")
            fim=1

        #empates
        elif tentativa == compu:
            print("Houve um empate")
            fim=1
            
    print("Fim")
    
    

# Executa o jogo
jokenpô()
