N1=float(input("Número 1: \n"))
N2=float(input("Número 2: \n"))
D=0
if (N1>N2):
    D=N1-N2
    print(f"A diferença entre {N1} e {N2} é {D}")
else:
    D=N2-N1
    print(f"A diferença entre {N2} e {N1} é {D}")
