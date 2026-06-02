import java.util.Scanner;

public class EscolaControl {
    public static void main(String[] args) {
        // 1. Instanciar o Scanner para ler dados do teclado
        Scanner scanner = new Scanner(System.in);
        
        // 2. Criar vetores para armazenar alunos e professores 
        // (Assumindo um limite de 100 como exemplo, ajuste conforme necessário)
        Aluno[] alunos = new Aluno[5];
        Professor[] professores = new Professor[5];
        
        // Variáveis de controle
        int opcao = 0;
        int totalAlunos = 0;
        int totalProfessores = 0;

        // 3. Exibir o menu e repetir até o usuário escolher sair (opção 4)
        while (!entrada.equalsIgnoreCase("sair")) {
            System.out.print("----------------------------");
            System.out.println("\nO que deseja fazer? Digite:");
            String[] menus = {
                "\n1 - Cadastrar aluno",
                "2 - Cadastrar professor",
                "3 - Listar alunos",
                "4 - Listar professores",
                "5 - Buscar aluno por nome",
                "6 - Buscar professor por nome",
                "7 - Exibir dados completos",
                "8 - Sair\n ",
            };
            for (String menu : menus) {
                System.out.println(menu);
            }
            
            opcao = scanner.nextInt();
            scanner.nextLine(); // Limpa o buffer do teclado após ler um número

            switch (opcao) {
                case 1:
                    System.out.println("-> Cadastrar aluno");
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
                    break;
                case 2:
                    System.out.println("-> Funcionalidade de cadastro de professor em breve.");
                    // Lógica para adicionar professor aos vetores viria aqui
                    break;
                case 3:
                    System.out.println("-> Exibindo cadastros atuais...");
                    // Lógica para listar alunos e professores viria aqui
                    break;
                case 4:
                    System.out.println("Saindo do sistema... Até logo!");
                    break;
                case 5:
                    System.out.println("Saindo do sistema... Até logo!");
                    break;
                case 6:
                    System.out.println("Saindo do sistema... Até logo!");
                    break;
                case 7:
                    System.out.println("Saindo do sistema... Até logo!");
                    break;
                case 8:
                    System.out.println("Saindo do sistema... Até logo!");
                    break;
                default:
                    System.out.println("Opção inválida! Tente novamente.");
            }
        }

        // Fecha o scanner para liberar recursos
        scanner.close();
    }
}
