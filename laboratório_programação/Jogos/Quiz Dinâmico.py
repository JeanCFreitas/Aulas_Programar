#Crie um jogo de perguntas e respostas a partir de uma lista de questões com múltiplas alternativas (ou verdadeiro/falso).
#O sistema deve apresentar uma pergunta de cada vez, permitir que o usuário selecione 
#uma resposta e, em seguida, informar se a resposta está correta, atualizando uma pontuação.

def exibir_pergunta(pergunta, alternativas, resposta):
    print("\n" + pergunta)
    for i, alternativa in enumerate(alternativas, 1):
        print(f"{i}. {alternativa}")
    
    while True:
        try:
            escolha = int(input("\nEscolha a alternativa (1/2/3/4): "))
            if 1 <= escolha <= len(alternativas):
                break
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")
    
    return escolha == resposta

def jogo_perguntas():
    perguntas = [
        {
            "pergunta": "Qual é a capital do Brasil?",
            "alternativas": ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"],
            "resposta": 3
        },
        {
            "pergunta": "O que é Python?",
            "alternativas": ["Uma cobra", "Uma linguagem de programação", "Uma árvore", "Um tipo de software"],
            "resposta": 2
        },
        {
            "pergunta": "A Terra é plana? (Verdadeiro ou Falso)",
            "alternativas": ["Verdadeiro", "Falso"],
            "resposta": 2
        },
        {
            "pergunta": "Quem pintou a Mona Lisa?",
            "alternativas": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
            "resposta": 3
        },
        {
            "pergunta": "Pikachu é amarelo?",
            "alternativas": ["Verdadeiro", "Falso"],
            "resposta": 1
        }
    ]
    
    pontuacao = 0
    
    print("Quiz Dinâmico!")
    for pergunta in perguntas:
        acertou = exibir_pergunta(pergunta["pergunta"], pergunta["alternativas"], pergunta["resposta"])
        
        if acertou:
            print("Resposta correta!")
            pontuacao += 1
        else:
            print(f"Resposta errada! A resposta correta era: {pergunta['alternativas'][pergunta['resposta'] - 1]}")
    
    print(f"\nVocê terminou o jogo com {pontuacao} ponto(s).")
    if pontuacao == len(perguntas):
        print("Parabéns, você acertou todas as perguntas!")
    else:
        print(f"Você errou {len(perguntas) - pontuacao} pergunta(s).")

# Chama a função para rodar o jogo
jogo_perguntas()