typechart = {
    "normal":      {"lutador": 2, "fantasma": 0},
    "fogo":        {"água": 2, "planta": 0.5, "gelo": 0.5, "inseto": 0.5, "fogo": 0.5, "rocha": 2, "terra": 2},
    "água":        {"fogo": 0.5, "água": 0.5, "elétrico": 2, "planta": 2, "gelo": 0.5},
    "elétrico":    {"terra": 2, "elétrico": 0.5, "voador": 0.5},
    "planta":      {"fogo": 2, "água": 0.5, "elétrico": 0.5, "gelo": 2, "voador": 2, "inseto": 2, "planta": 0.5, "veneno": 2},
    "gelo":        {"fogo": 2, "gelo": 0.5, "lutador": 2, "rocha": 2, "aço": 2},
    "lutador":     {"voador": 2, "psíquico": 2, "inseto": 0.5, "rocha": 0.5, "sombrio": 0.5, "fantasma": 0},
    "veneno":      {"terra": 2, "psíquico": 2, "planta": 0.5, "lutador": 0.5, "veneno": 0.5, "fantasma": 0.5},
    "terra":       {"água": 2, "planta": 2, "gelo": 2, "veneno": 0.5, "rocha": 0.5, "elétrico": 0},
    "voador":      {"elétrico": 2, "gelo": 2, "rocha": 2, "planta": 0.5, "lutador": 0.5, "inseto": 0.5, "terra": 0},
    "psíquico":    {"inseto": 2, "fantasma": 2, "sombrio": 2, "lutador": 0.5, "psíquico": 0.5},
    "inseto":      {"fogo": 2, "voador": 2, "pedra": 2, "planta": 0.5, "lutador": 0.5, "terra": 0.5},
    "rocha":       {"água": 2, "planta": 2, "lutador": 2, "terra": 2, "normal": 0.5, "fogo": 0.5, "veneno": 0.5, "voador": 0.5},
    "fantasma":    {"fantasma": 2, "sombrio": 2, "veneno": 0.5, "inseto": 0.5, "normal": 0, "lutador": 0},
    "dragão":      {"gelo": 2, "dragão": 2, "fada": 2, "fogo": 0.5, "água": 0.5, "elétrico": 0.5, "planta": 0.5},
    "sombrio":     {"lutador": 2, "inseto": 2, "fada": 2, "fantasma": 0.5, "sombrio": 0.5, "psíquico": 0},
    "aço":         {"fogo": 2, "lutador": 2, "terra": 2, "normal": 0.5, "planta": 0.5, "gelo": 0.5, "inseto": 0.5,
                    "rocha": 0.5, "dragão": 0.5, "aço": 0.5, "veneno": 0, "fada": 0.5},
    "fada":        {"veneno": 2, "aço": 2, "lutador": 0.5, "sombrio": 0.5, "dragão": 0},
    "nenhum":      {}
}

tipos_validos = list(typechart.keys())

def calcular_defesa(tipo1, tipo2=None):
    defesa = {}
    for ataque in tipos_validos:
        m1 = typechart.get(tipo1, {}).get(ataque, 1)
        m2 = typechart.get(tipo2, {}).get(ataque, 1) if tipo2 else 1
        total = m1 * m2
        defesa[ataque] = total

    imune = [t for t, m in defesa.items() if m == 0]
    resistente = [t for t, m in defesa.items() if m == 0.25]
    pouco_efetivo = [t for t, m in defesa.items() if m == 0.5]
    neutro = [t for t, m in defesa.items() if m == 1]
    super_efetivo = [t for t, m in defesa.items() if m == 2]
    ultra_efetivo = [t for t, m in defesa.items() if m == 4]

    print(f"\nDefesas para o tipo {' e '.join([tipo1, tipo2] if tipo2 else [tipo1])}:\n")
    if imune:
        print("Imune (0x):", ", ".join(imune))
    if resistente:
        print("Resistente (0.25x):", ", ".join(resistente))
    if pouco_efetivo:
        print("Pouco efetivo (0.5x):", ", ".join(pouco_efetivo))
    if neutro:
        print("Neutro (1x):", ", ".join(neutro))
    if super_efetivo:
        print("Fraco (2x):", ", ".join(super_efetivo))
    if ultra_efetivo:
        print("Muito fraco (4x):", ", ".join(ultra_efetivo))
    

def main():
    print("=== Calculadora de Defesa de Tipos Pokémon ===")
    print("Tipos disponíveis:", ", ".join(tipos_validos))
    tipo1 = input("Digite o primeiro tipo: ").strip().lower()
    tipo2 = input("Digite o segundo tipo (ou pressione Enter para deixar vazio): ").strip().lower()

    if tipo1 not in tipos_validos or (tipo2 and tipo2 not in tipos_validos):
        print("Erro: Um ou mais tipos inválidos.")
        return
    if tipo1 == tipo2:
        tipo2 = ""

    calcular_defesa(tipo1, tipo2 if tipo2 else None)

if __name__ == "__main__":
    main()
