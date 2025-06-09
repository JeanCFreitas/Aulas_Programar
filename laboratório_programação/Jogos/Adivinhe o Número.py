#O sistema gera um número aleatório dentro de um intervalo definido (ex: 1 a 100).
#O usuário tenta adivinhar qual é o número. Após cada tentativa, o sistema informa se 
#o palpite do usuário foi muito alto, muito baixo ou se acertou. 
#Opcionalmente, pode contar o número de tentativas.

import random

def adivinhação():
    numero = random.randint(1, 100)
    tentativas = 0
    chute = 0
    print("Adivinhe o número entre 1 e 100.\n")
    perto = 0

    while chute!=numero:
        
        chute = int(input("Digite seu palpite: "))
        tentativas += 1
        perto = numero - chute
        if chute < 1 or chute > 100:
            print("Por favor, digite um número entre 1 e 100.")
        elif chute < numero:
            print("Muito baixo. Tente novamente.")
            perto = numero - chute
            if perto <=5:
                print(f"Mais {perto} digitos para cima")
        elif chute > numero:
            print("Muito alto. Tente novamente.")
            perto = chute - numero
            if perto <=5:
                print(f"Mais {perto} digitos para baixo")


    print(f"Parabéns! Você descobriu o número {numero} em {tentativas} tentativa(s)!")
            
# Executa o jogo
adivinhação()