Temperatura=float(input('Digite a temperatura que deseja converter: '))
CouF = int(input("Digite para oq deseja converter, 1 para F e 2 para C: "))

if (CouF == 1):
    F = (CouF* 1.8 )+32
    print (f'{F}ºF')

elif (CouF == 2):
    C = (CouF - 32 ) * 5/9
    print (f'{C}ºC')

else:
    print('Error')