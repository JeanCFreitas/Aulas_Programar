import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class Atividade2 {

    // Numero maximo de alunos
    static final int MAX_ALUNOS = 5;

    // Arrays paralelos para armazenar os dados dos alunos
    static String[] nomes  = new String[MAX_ALUNOS];
    static Integer[] idades = new Integer[MAX_ALUNOS];

    // Contador de alunos cadastrados (tipo primitivo int)
    static int totalAlunos = 0;
    
    // Inicia o programa
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String entrada = "";

        // O loop continua enquanto a entrada for diferente de "sair"
        while (!entrada.equalsIgnoreCase("sair")) {
            System.out.print("----------------------------");
            System.out.println("\nO que deseja fazer? Digite:");
            String[] menus = {
                "\n1 - Cadastrar aluno",
                "2 - Listar alunos",
                "3 - Buscar aluno por nome",
                "4 - Calcular media de idade",
                "5 - Exibir data/hora atual",
                "6 - Sair\n",
            };
            for (String menu : menus) {
                System.out.println(menu);
            }

            // Decidir qual opção do menu será usada
            int decisao = 0;
            decisao = Integer.parseInt(scanner.nextLine().trim());
            if (decisao == 1) {
                
                // Ver se o limite de alunos cadastrados foi atingido
                if (totalAlunos >= MAX_ALUNOS) {
                    System.out.println("Erro: Limite de " + MAX_ALUNOS + " alunos atingido.\n");
                    continue;
                } else {
                    System.out.println("Existem " + totalAlunos + " alunos cadastrados");
                }
                
                // Inserir o nome do aluno formatado da maneira correta
                System.out.println("Digite o nome do aluno:");
                String nomeDigitado = scanner.nextLine().trim().toLowerCase();
                String nome = "";
                boolean proximaMaiuscula = true;
                for (int i = 0; i < nomeDigitado.length(); i++) {
                    char c = nomeDigitado.charAt(i);
                    if (c == ' ') {
                        nome += c;
                        proximaMaiuscula = true;
                    } else if (proximaMaiuscula) {
                        nome += Character.toUpperCase(c);
                        proximaMaiuscula = false;
                    } else {
                        nome += c;
                    }
                }

                // Inserir a idade do aluno
                int idade = 0;
                do {
                    System.out.println("Digite a idade do aluno (entre 3 e 19): ");
                    idade = Integer.parseInt(scanner.nextLine().trim());
                    if (idade < 3 || idade > 19) {
                        System.out.println("[AVISO] Idade invalida. Digite um valor entre 3 e 19.");
                    }
                } while (idade < 3 || idade > 19);

                // Armazena as informações dos alunos em dois arrays
                nomes[totalAlunos] = nome;
                idades[totalAlunos] = idade;

                // Da Print no cadastro do aluno
                System.out.println("--- CADASTRO REALIZADO ---");
                System.out.println("Aluno: " + nome);
                System.out.println("Idade: " + idade);
                
                // Conta quantos alunos já foram cadastrados
                totalAlunos += 1;
                
            } else if (decisao == 2) {
                // Mostra os nomes e idades de todos os alunos ou uma mensagem de erro
                if (totalAlunos == 0) {
                    System.out.println("Erro: Nenhum aluno cadastrado ainda.\n");
                } else {
                    System.out.println("\n--- LISTA DE ALUNOS CADASTRADOS | " + totalAlunos + " ALUNOS NO TOTAL ---");
                    System.out.printf("%-4s %-20s %-7s%n", "#", "Nome", "Idade");
                    for (int i = 0; i < totalAlunos; i++) {
                        System.out.printf("%-4d %-20s %-7d%n",
                                (i + 1),
                                nomes[i],
                                idades[i]);
                    }
                }

            } else if (decisao == 3) {
                // Permite a pesquisa dos alunos pelo nome (só é necessário o primeiro nome)
                if (totalAlunos == 0) {
                    System.out.println("[ERRO] Nenhum aluno cadastrado");
                    continue;
                }
                System.out.println("Digite o nome do aluno:");
                String busca = scanner.nextLine().trim().toLowerCase();
                boolean encontrou = false;
                for (int i = 0; i < totalAlunos; i++) {
                    if (nomes[i].toLowerCase().contains(busca)) {
                        encontrou = true;
                        System.out.println("Aluno encontrado -> Nome: " + nomes[i] + " | Idade: " + idades[i]);
                    }
                }
                if (!encontrou) {
                    System.out.println("[ERRO] Aluno não encontrado");
                }

            } else if (decisao == 4) {
                // Mostra a média da idade dos alunos
                if (totalAlunos == 0) {
                    System.out.println("[ERRO] Nenhum aluno cadastrado");
                    continue;
                }
                double soma = 0;
                for (int i = 0; i < totalAlunos; i++) {
                    soma += idades[i];
                }
                double mediaIdade = soma / totalAlunos;
                System.out.printf("Media de idade da turma: " + mediaIdade);

            } else if (decisao == 5) {
                // Mostra a data e a hora
                // Nota importante: Fiz esse programa no site Programiz por não conseguir rodar Java no VSCode. Por algum motivo, o 
                // LocalDateTime pega um horário 2 horas adiantado em relação ao horário de brasilia. Não sei como arrumar isso e 
                // aparentemente é um problema no site que usei e não no programa
                LocalDateTime agora = LocalDateTime.now();
                DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");
                System.out.println("Data/hora atual: " + agora.format(formatter));

            } else if (decisao == 6) {
                entrada = "sair";
            // Evita erro com valor inválido
            } else {
                System.out.println("Valor invalido");
            }
        }
        //Fecha o programa
        System.out.println("Programa encerrado.");
        scanner.close();
    }
}
//Perguntas 8 e 10
//8 - Qual a diferença entre int e Integer?
// "int" é um tipo primitivo. Armazena o valor diretamente na memória, é mais rápido e não pode ser null. 
// "Integer" é uma classe wrapper. Ela "embrulha" o int dentro de um objeto, o que permite usar métodos utilitários e aceitar null.

//10 - Qual a diferença entre while e do-while?
// "while" verifica a condição antes de executar. Se a condição já começar falsa, o bloco nunca executa. 
// "do-while" executa o bloco primeiro, depois verifica a condição. Isso garante que o bloco execute pelo menos uma vez.