#Criar Lista
lista = list ([1,3,5,7,9,2,4,6,8,10])
soma=0
lista.sort()
print(f"Lista em ordem crescente: {lista}")

print(f"O maior digito da lista é {max(lista)}")
print(f"O menor digito da lista é {min(lista)}")

for lista in lista:
    soma += lista
print (f"A soma de todos os digitos da lista é {soma}")