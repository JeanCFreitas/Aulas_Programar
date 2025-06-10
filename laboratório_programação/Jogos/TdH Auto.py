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

#Example usage
n = int(input("Enter the number of disks: "))
torre(n, 'A', 'C', 'B')