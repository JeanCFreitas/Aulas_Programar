tempo = float(input("Digite o tempo gasto na viagem (em horas):")) 
velocidade_media = float(input("Digite a velocidade média durante a viagem (em km/h):"))
distancia = tempo * velocidade_media
litros_usados = distancia/12
print("Velocidade média:", velocidade_media, "km/h")
print ("Tempo gasto na viagem:", tempo,"horas")
print ("Distância percorrida:", distancia,"km")
print("Quantidade de litros usada na viagem:", '%.2f' %litros_usados, "litros")