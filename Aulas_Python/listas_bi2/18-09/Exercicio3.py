lista = list (['Ana','Carlos','Beatriz','Daniel','Elisa'])

lista[2]='Bruna'

if 'Carlos' in lista:
    print('Carlos está na lista')
else:
    print('Carlos não está na lista')

print(f"Numero de vezes que Ana aparece na lista: {lista.count('Ana')}")

print(f'Lista após trocar Beatriz por Bruna: {lista}')