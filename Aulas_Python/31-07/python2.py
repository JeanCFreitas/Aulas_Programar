n1=float(input('Digite primeira nota:'))
n2=float(input('Digite segunda nota:'))
n3=float(input('Digite terceira nota:'))
media=(n1+n2+n3)/3
if media>=6.0:
    print(f"Parabéns! Você foi aprovado com média {media}")
else:
    print(f"Infelizmente você não foi aprovado com média {media}")
if media>10:
    print("Nota invalida")