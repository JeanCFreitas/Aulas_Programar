A=float(input('Digite primeiro numero:'))
B=float(input('Digite segundo numero:'))
C=float(input('Digite terceiro numero:'))
if (A>B>C):
    print(f'Maior número:{A} / Menor número:{C} / Número do meio:{B}. ')
elif (A>C>B):
    print(f'Maior número:{A} / Menor número:{B} / Número do meio:{C}.')
elif (B>A>C):
    print(f'Maior número:{B} / Menor número:{C} / Número do meio:{A}.')
elif (B>C>A):
    print(f'Maior número:{B} / Menor número:{A} / Número do meio:{C}.')
elif (C>B>A):
    print(f'Maior número:{C} / Menor número:{A} / Número do meio:{B}.')
elif (C>A>B):
    print(f'Maior número:{C} / Menor número:{B} / Número do meio:{C}.')