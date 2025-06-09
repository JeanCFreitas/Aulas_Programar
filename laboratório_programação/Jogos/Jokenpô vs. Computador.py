#Desenvolva o clássico jogo onde o usuário escolhe entre Pedra, Papel ou Tesoura.
#O computador fará a sua escolha aleatoriamente. O sistema então determina e exibe 
#o vencedor da rodada (usuário, computador ou empate) e,
#opcionalmente, mantém um placar

import random


def jokenpô():
    tentativa = 0
    fim=1
    print("Jokenpô. 1 = Pedra, 2 = Papel, 3 = Tesoura.\n")
    score_player=0
    score_compu=0

    while fim==1:
        compu = random.randint(1,3)
        tentativa = int(input("Digite seu palpite: "))
        #derrotas
        if tentativa == 1 and compu == 2:
            print("Sua Pedra foi embrulhada, você perdeu.")
            score_compu+=1
            print("Deseja jogar novamente?")
            fim = int(input("1 = Sim, 0 = Não\n"))
        elif tentativa == 2 and compu == 3:
            print("Seu Papel foi cortado, você perdeu.")
            score_compu+=1
            print("Deseja jogar novamente?")
            fim = int(input("1 = Sim, 0 = Não\n"))
        elif tentativa == 3 and compu == 1:
            print("Sua Tesoura foi quebrada, você perdeu.")
            score_compu+=1
            print("Deseja jogar novamente?")
            fim = int(input("1 = Sim, 0 = Não\n"))
        
    
        #vitórias
        elif tentativa == 2 and compu == 1:
            print("Seu Papel embrulhou a Pedra, você venceu.")
            score_player+=1
            print("Deseja jogar novamente?")
            fim = int(input("1 = Sim, 0 = Não\n"))
        elif tentativa == 3 and compu == 2:
            print("Sua Tesoura cortou o Papel, você venceu.")
            score_player+=1
            print("Deseja jogar novamente?")
            fim = int(input("1 = Sim, 0 = Não\n"))
        elif tentativa == 1 and compu == 3:
            print("Sua Pedra quebrou a Tesoura, você venceu.")
            score_player+=1
            print("Deseja jogar novamente?")
            fim = int(input("1 = Sim, 0 = Não\n"))

        #empates
        elif tentativa == compu:
            print("Houve um empate")
            print("Deseja jogar novamente?")
            fim = int(input("1 = Sim, 0 = Não\n"))
        elif tentativa !=1 and tentativa !=2 and tentativa !=3:
            print("Você não jogou a sua mão.")
            print("Deseja jogar novamente?")
            fim = int(input("1 = Sim, 0 = Não\n"))
            
    print(f"Placar final: Maquina [{score_compu}] vs [{score_player}] Player")
    
    

# Executa o jogo
jokenpô()
