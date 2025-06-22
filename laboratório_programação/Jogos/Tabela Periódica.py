import re

# Tabela periódica com massas molares arredondadas (inteiros)
tabela_periodica = {
    "H": 1,
    "He": 4,
    "Li": 7,
    "Be": 9,
    "B": 11,
    "C": 12,
    "N": 14,
    "O": 16,
    "F": 19,
    "Ne": 20,
    "Na": 23,
    "Mg": 24,
    "Al": 27,
    "Si": 28,
    "P": 31,
    "S": 32,
    "Cl": 35,
    "Ar": 40,
    "K": 39,
    "Ca": 40,
    "Fe": 56,
    "Cu": 64,
    "Zn": 65,
    "Ag": 108,
    "Au": 197,
    "Pb": 207
}

# Função para calcular massa molar de um composto
def calcular_massa_molar(composto):
    padrao = r'([A-Z][a-z]*)(\d*)'
    elementos = re.findall(padrao, composto)
    
    massa_total = 0
    for (elemento, quantidade) in elementos:
        if elemento not in tabela_periodica:
            print(f"Elemento '{elemento}' não encontrado na tabela periódica.")
            return None
        quantidade = int(quantidade) if quantidade else 1
        massa = tabela_periodica[elemento] * quantidade
        massa_total += massa

    return round(massa_total)

# 🚀 Testando
composto = input("Digite o composto químico (ex: H2O, CO2, C6H12O6): ")
massa = calcular_massa_molar(composto)

if massa is not None:
    print(f"A massa molar de {composto} é {massa} g/mol")