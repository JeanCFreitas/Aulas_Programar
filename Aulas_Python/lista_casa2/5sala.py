A=float(input('Digite primeiro numero:'))
B=float(input('Digite segundo numero:'))
C=float(input('Digite terceiro numero:'))
if (A>B>C):
    print(f'Maior número:{A} / Número do meio:{B} / Menor número:{C}. ')
elif (A>C>B):
    print(f'Maior número:{A} / Número do meio:{C} / Menor número:{B}.')
elif (B>A>C):
    print(f'Maior número:{B} / Número do meio:{A} / Menor número:{C}.')
elif (B>C>A):
    print(f'Maior número:{B} / Número do meio:{C} / Menor número:{A}.')
elif (C>B>A):
    print(f'Maior número:{C} / Número do meio:{B} / Menor número:{A}.')
elif (C>A>B):
    print(f'Maior número:{C} / Número do meio:{C} / Menor número:{B}.')