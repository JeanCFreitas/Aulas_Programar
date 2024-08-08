n1=float(input('Digite primeira nota:\n'))
n2=float(input('Digite segunda nota:\n'))
n3=float(input('Digite terceira nota:\n'))
media=(n1+n2+n3)/3
if media>10:
    print("Nota invalida")
elif media>=6.0:
    print(f"Parabéns! Você foi aprovado com média {media}")
else:
    print(f"Infelizmente você não foi aprovado com média {media}")