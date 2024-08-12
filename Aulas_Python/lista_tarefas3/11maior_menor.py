A=float(input('Digite primeiro numero:'))
B=float(input('Digite segundo numero:'))
C=float(input('Digite terceiro numero:'))
D=float(input('Digite quarto numero:'))
E=float(input('Digite quinto numero:'))
if (A>B or A>C or A>D or A>E):
    print(f'Maior número:{A}')
elif (A<B or A<C or A<D or A<E):
    print(f'Menor número:{A}')
elif (B>A or B>C or B>D or B>E):
    print(f'Maior número:{B}')
elif (B<A or B<C or B<D or B<E):
    print(f'Menor número:{B}')
elif (C>A or C>B or C>D or C>E):
    print(f'Maior número:{C}')
elif (C<A or C<B or C<D or C<E):
    print(f'Menor número:{C}')
elif (D>A or D>C or D>B or D>E):
    print(f'Maior número:{D}')
elif (D<A or D<C or D<B or D<E):
    print(f'Menor número:{D}')
elif (E>A or E>C or E>D or E>B):
    print(f'Maior número:{E}')
elif (E<A or E<C or E<D or E<B):
    print(f'Menor número:{E}')