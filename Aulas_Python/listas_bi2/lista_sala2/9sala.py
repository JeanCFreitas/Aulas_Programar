A=int(input("1º Número: \n"))
B=int(input("2º Número: \n"))


if (A%4==0 and A%5==0):
    print(f"{A} É divisível por 4 e 5!")
elif (A%4==0):
    print(f"{A} É divisível apenas por 4!")
elif (A%5==0):
    print(f"{A} É divisível apenas por 5!")
else:
    print(f"{A} não é divisível por 4 ou 5!")

if (B%4==0 and B%5==0):
    print(f"{B} É divisível por 4 e 5!")
elif (B%4==0):
    print(f"{B} É divisível apenas por 4!")
elif (B%5==0):
    print(f"{B} É divisível apenas por 5!")
else:
    print(f"{B} não é divisível por 4 ou 5!")