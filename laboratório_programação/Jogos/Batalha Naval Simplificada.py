#Implemente uma versão onde o computador posiciona os seus navios secretamente num
#tabuleiro de dimensões fixas (ex: 10x10). O usuário clica nas células do tabuleiro 
#para tentar acertar os navios do computador. O sistema informa se o tiro acertou na 
#água, num navio ou afundou um navio. O objetivo é afundar todos os navios do computador.

# Não consegui fazer

import random

# Função para criar o tabuleiro vazio
def criar_tabuleiro():
    return [[' ' for _ in range(7)] for _ in range(7)]

# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    print("  A B C D E F G")
    for i, linha in enumerate(tabuleiro):
        print(f"{i + 1} {' '.join(linha)}")

# Função para converter as letras de colunas para índices
def coluna_para_indice(coluna):
    return ord(coluna.upper()) - ord('A')

# Função para posicionar os navios do computador
def posicionar_navios():
    navios = []
    while len(navios) < 3:  # O computador terá 3 navios
        linha = random.randint(0, 6)
        coluna = random.randint(0, 6)
        if (linha, coluna) not in navios:
            navios.append((linha, coluna))
    return navios

# Função principal do jogo
def jogo_batalha_naval():
    # Inicialização dos tabuleiros
    tabuleiro_usuario = criar_tabuleiro()
    tabuleiro_computador = criar_tabuleiro()
    
    # Posicionando navios do computador
    navios_computador = posicionar_navios()
    navios_afundados = 0

    print("Bem-vindo ao Jogo da Batalha Naval!")
    
    while navios_afundados < 3:
        exibir_tabuleiro(tabuleiro_usuario)
        
        # O jogador faz uma jogada
        jogada = input("Digite o quadrado: ").strip()
        try:
            coluna, linha = jogada.split()
            linha = int(linha) - 1
            coluna = coluna_para_indice(coluna)
            if not (0 <= linha < 7 and 0 <= coluna < 7):
                print("Coordenada inválida! Tente novamente.")
                continue
        except (ValueError, IndexError):
            print("Entrada inválida! Tente novamente.")
            continue

        # Verificando se o jogador já atirou nessa célula
        if tabuleiro_usuario[linha][coluna] != ' ':
            print("Você já tentou essa coordenada! Tente novamente.")
            continue

        # Verificando se acertou um navio
        if (linha, coluna) in navios_computador:
            tabuleiro_usuario[linha][coluna] = 'X'  # Marca como acerto
            navios_computador.remove((linha, coluna))  # Remove o navio atingido
            print("Acertou um navio!")
            
            # Verificando se afundou um navio
            if len(navios_computador) == 0:
                print("Parabéns! Você afundou todos os navios!")
                break
        else:
            tabuleiro_usuario[linha][coluna] = 'O'  # Marca como água
            print("Água! Não acertou nada.")
        
        # Atualizando a quantidade de navios afundados
        if len(navios_computador) == 0:
            navios_afundados = 3
    
    print("Fim do jogo!")

# Chama a função para rodar o jogo
jogo_batalha_naval()