saldo=float(input('Digite um saldo de mil, 3mil ou 5mil reais: \n'))

if (saldo == 1000):
    print(f'A tarifa do seu saldo é igual a: R$ {saldo-(0.2*saldo)}')

elif (saldo == 5000):
    print(f'A tarifa do seu saldo é igual a: R$ {saldo-(0.3*saldo)}')
     
elif (saldo == 3000):
    print(f'A tarifa do seu saldo é igual a: R$ {saldo-(0.25*saldo)}')
    
else:
    print('VALOR INVALIDO')