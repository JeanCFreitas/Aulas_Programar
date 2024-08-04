n1=float(input('Digite primeira nota:'))
n2=float(input('Digite segunda nota:'))
media = (n1 + n2)/2
if media>=6.0:
    print(f"Parabéns! Você foi aprovado com média {media}")
else:
    print("fara exame para nova média")
    e=float(input('Digite nota exame:'))
    nmedia=media+e
if nmedia>=5.0:
    print(f"Parabéns! Você foi aprovado com nova média {nmedia}")
else: 
    print(f"Infelizmente você não foi aprovado com nova média {nmedia}")
    
