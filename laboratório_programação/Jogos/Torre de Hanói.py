#Desenvolva uma interface onde o usuário possa interativamente mover os discos 
#(por exemplo, 3 a 5 discos) entre as três hastes. O sistema deve validar cada 
# movimento de acordo com as regras da Torre de Hanói (só se pode mover um disco
#de cada vez, e um disco maior nunca pode ser colocado sobre um menor).
# O objetivo é que o usuário resolva o quebra-cabeça.

# Apenas Teste

#def torre(n, source, target, aux):
#    if n == 1:
#        print(f"Move disk 1 from {source} to {target}")
#        return
    
    # Move n-1 disks from source to aux using target as auxiliary
#    torre(n - 1, source, aux, target)
    
    # Move the nth disk from source to target
#    print(f"Move disk {n} from {source} to {target}")
    
    # Move n-1 disks from aux to target using source as auxiliary
#    torre(n - 1, aux, target, source)

# Example usage
#n = int(input("Enter the number of disks: "))
#torre(n, 'A', 'C', 'B')

def mudar (mesa, nPecas):
    while True:
        try:
            src, dest = input("Faça sua mudança:\n\n<Nº ARGOLA FONTE> <Nº ARGOLA DESTINO>\n\n").split()
            src, dest = int(src)-1, int(dest)-1
            if 0 <= src != dest <= 2:
                break
            else:
                raise Exception
        except:
            print ("MOVIMENTO INVÁLIDO")
            return False
    try:
        u = mesa[src][-1]
    except:
        print ("MOVIMENTO INVÁLIDO")
        return False
    if (len(mesa[dest]) == 0 or (u < mesa[dest][-1] and len(mesa[dest]) != nPecas)):
        mesa[dest].append(u)
        mesa[src].pop()
    else:
        print ("MOVIMENTO INVÁLIDO")
    if len(mesa[dest]) == nPecas:
        return True
    return False


def jogo():
    n = int(input("Número de peças: "))
    print()
    mesa = [[i for i in range(n, 0, -1)], [], []]
    while True:
        for i in range(n-1, -1, -1):
            for j in range (0, 3):
                try:
                    print (mesa[j][i], "   ", end='')
                except:
                    print ("     ", end='')
            print()
        print("|____|____|")
        if mudar(mesa, n):
            return True

jogo()