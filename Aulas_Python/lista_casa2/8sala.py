print("3 números inteiros divisíveis por 2 e 3")
A=int(input("1º Número: "))
B=int(input("2º Número: "))
C=int(input("3º Número: "))


if (A%3==0 and A%2==0):
    print(f"{A} É divisível por 2 e 3!")
else:
    print(f"{A} não é divisível por 2 e 3!")
if (B%3==0 and B%2==0):
    print(f"{B} É divisível por 2 e 3!")
else:
    print(f"{B} não é divisível por 2 e 3!")
if (C%3==0 and C%2==0):
    print(f"{C} É divisível por 2 e 3!")
else:
    print(f"{C} não é divisível por 2 e 3!")