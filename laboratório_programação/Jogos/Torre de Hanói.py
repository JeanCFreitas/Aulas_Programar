#Desenvolva uma interface onde o usuário possa interativamente mover os discos 
#(por exemplo, 3 a 5 discos) entre as três hastes. O sistema deve validar cada 
# movimento de acordo com as regras da Torre de Hanói (só se pode mover um disco
#de cada vez, e um disco maior nunca pode ser colocado sobre um menor).
# O objetivo é que o usuário resolva o quebra-cabeça.

# Recursive Python function to solve the tower of hanoi

def torre(n, source, target, aux):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
    # Move n-1 disks from source to aux using target as auxiliary
    torre(n - 1, source, aux, target)
    
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    
    # Move n-1 disks from aux to target using source as auxiliary
    torre(n - 1, aux, target, source)

# Example usage
n = int(input("Enter the number of disks: "))
torre(n, 'A', 'C', 'B')