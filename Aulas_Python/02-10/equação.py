import math
a = float(input("Digite A:"))
b = float(input("Digite B:"))
c = float(input("Digite C:"))
    
if a == 0:
    print('Não é equação de segundo grau')
delta=b**2-4*a*c
if delta<0:
    print('não é equação')
elif delta == 0:
    print('nao')
else:
    raiz1= (-b + math.sqrt(delta))/(2*a)
    raiz2= (-b - math.sqrt(delta))/(2*a)
    print(f'A equação possui duas raizes reais: {raiz1} e {raiz2}')