#Implemente o jogo da forca utilizando uma lista predefinida de palavras.
#A cada rodada, uma palavra é escolhida aleatoriamente. O usuário tenta adivinhar as letras.
#A interface deve mostrar a palavra parcialmente descoberta, as letras já tentadas (corretas e incorretas)
#e o número de tentativas restantes. O usuário perde se cometer 6 erros.

import random

def escolher_palavra(lista_palavras):
    return random.choice(lista_palavras).upper()

def mostrar_palavra(palavra, letras_certas):
    return ' '.join([letra if letra in letras_certas else '_' for letra in palavra])

def jogo_da_forca():
    palavras = ["sagaz", "termo", "nobre", "vigor", "poder", "carta", "clube"]
    palavra = escolher_palavra(palavras)
    letras_tentadas = set()
    letras_certas = set()
    letras_erradas = set()
    erros = 0

    print("Bem-vindo ao Termo 2!")

    while erros < 6 and set(palavra) != letras_certas:
        print("\nPalavra:", mostrar_palavra(palavra, letras_certas))
        print("Letras tentadas:", ' '.join(sorted(letras_tentadas)))
        print("Letras erradas:", ' '.join(sorted(letras_erradas)))
        print(f"Tentativas restantes: {6 - erros}")
        tentativa = input("Digite uma letra: ").strip().upper()

        if not tentativa.isalpha() or len(tentativa) != 1:
            print("Entrada inválida. Digite apenas uma letra.")
            continue

        if tentativa in letras_tentadas:
            print("Você já tentou essa letra.")
            continue

        letras_tentadas.add(tentativa)

        if tentativa in palavra:
            letras_certas.add(tentativa)
            print("Boa! Letra correta.")
        else:
            letras_erradas.add(tentativa)
            erros += 1
            print("Letra incorreta.")

    if set(palavra) == letras_certas:
        print("\nParabéns! Você ganhou! A palavra era:", palavra)
    else:
        print("\nVocê perdeu! A palavra era:", palavra)

jogo_da_forca()