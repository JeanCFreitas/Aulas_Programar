horas = float(input("Digite o tempo da viagem (em horas):")) 
velocidade = float(input("Digite a velocidade média (em km/h):"))
distancia = horas * velocidade
litros_usados = distancia/12
print("Velocidade média:", velocidade, "km/h")
print ("Tempo gasto na viagem:", horas,"horas")
print ("Distância percorrida:", distancia,"km")
print("Quantidade de litros usada na viagem:", '%.2f' %litros_usados, "litros")