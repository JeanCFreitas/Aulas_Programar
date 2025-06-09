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

    while chute!=numero:
        
        chute = int(input("Digite seu palpite: "))
        tentativas += 1

        if chute < 1 or chute > 100:
            print("Por favor, digite um número entre 1 e 100.")
        elif chute < numero:
            print("Muito baixo. Tente novamente.")
        elif chute > numero:
            print("Muito alto. Tente novamente.")
        if chute == numero+5 or chute == numero-5:
            print("Está chegando perto")

    print(f"Parabéns! Você descobriu o número {numero} em {tentativas} tentativa(s)!")
            
# Executa o jogo
adivinhação()