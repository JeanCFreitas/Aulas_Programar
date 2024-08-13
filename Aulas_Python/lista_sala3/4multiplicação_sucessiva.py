num=int(input('Digite um numero menor ou igual a 50:'))
if (0<num<=50):
    while(num<250):
        print(f'valor atual é {num}')
        num=num*3
elif (num<=0):
    print(f'ERRO: NÚMERO É MENOR OU IGUAL A 0')
else:
    print(f'ERRO: NÚMERO É MAIOR QUE 50')