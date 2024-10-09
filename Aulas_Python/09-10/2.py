def Contarc(texto):
    frequencia=0
    for caractere in texto:
        if caractere != "": #ignorar espaços
            if caractere in frequencia:
                frequencia[caractere] += 1
            else:
                frequencia[caractere] = 1
    return frequencia

texto = "python é top"
letra=(input('escolhe'))
Contagem = (texto)
print(Contagem.count (letra))