print('Digite 1 para Operação de Depósito')
print('Digite 2 para Operação de Saque')
print('Digite 3 para Operação de Extrato')
print('Digite 4 para Operação de Transfêrencia')
print('Digite qualquer outra coisa para Encerrar Operações')
extrato=0
extrato_deposito=0
extrato_saque=0
extrato_transferencia=0
escolha=float(input('Digite a Operação:\n'))
while (escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4):

    if (escolha==1):
        deposito=int(input('Deseja depositar quanto?:\n'))
        extrato=extrato + 1
        extrato_deposito=extrato_deposito+deposito
        escolha=int(input('Digite a próxima Operação:\n'))
    elif (escolha==2):
        saque=int(input('Deseja sacar quanto?:\n'))
        extrato=extrato + 1
        extrato_saque=extrato_saque+saque
        escolha=int(input('Digite a próxima Operação:\n'))
    elif (escolha==3):
        print(f'Extrato total: {extrato} ')
        if (extrato_deposito>0):
            print (f'Depósito total: {extrato_deposito}')
        if (extrato_saque>0):
            print (f'Saque total: {extrato_saque}')
        if (extrato_transferencia>0):
            print (f'Total de transferencia: {extrato_transferencia}')
        
        escolha=int(input('Digite a próxima Operação:\n'))
    elif (escolha==4):
        transferencia=int(input('Deseja transferir quanto?:\n'))
        extrato=extrato+1
        extrato_transferencia=extrato_transferencia+transferencia
        
        escolha=int(input('Digite a próxima Operação:\n'))
        
print('Obrigado por usar o Banco IFSP')