A = float(input("Digite o lado A do triângulo: "))
B = float(input("Digite o lado B do triângulo: "))
C = float(input("Digite o lado C do triângulo: "))

if (A==B and B==C):
        print("Esse triângulo é Equilátero!")
elif (A!=B and B!=C and C!=A):
        print("Esse triângulo é Escaleno!")
elif (A==B or B==C or C==A):
        print("Esse triângulo é Isósceles!")
else:
    print("Esses lados não formam um triângulo!")