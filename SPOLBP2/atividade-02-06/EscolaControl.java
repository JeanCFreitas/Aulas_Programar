import java.util.Scanner;

public class EscolaControl{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Aluno[] alunos = new Aluno[5];
        Professor[] professores = new Professor[5];
        int totalAlunos = 0;
        int totalProfessores = 0;

        int opcao;

        do {
            //por algum motivo, se nao colocar essa parte, o código não lembra os professores cadastrados
            System.out.print("----------------------------");
            System.out.println("\nInformações atuais do sistema:");
            System.out.println("Alunos: " + totalAlunos);
            System.out.println("Professores: " + totalProfessores);
            
            System.out.print("----------------------------");
            System.out.println("\nO que deseja fazer? Digite:");
            System.out.println("\n1 - Cadastrar aluno");
            System.out.println("2 - Cadastrar professor");
            System.out.println("3 - Listar alunos");
            System.out.println("4 - Listar professores");
            System.out.println("5 - Buscar aluno por nome");
            System.out.println("6 - Buscar professor por nome");
            System.out.println("7 - Exibir dados completos");
            System.out.println("8 - Sair\n ");
            System.out.print("Opção: ");
            opcao = scanner.nextInt();
            scanner.nextLine();
            switch (opcao) {

                case 1:
                    System.out.println("-> Cadastrar aluno");
                    if (totalAlunos >= alunos.length) {
                        System.out.println("[ERRO] Limite de alunos atingido");
                        break;
                    }

                    System.out.print("Nome do aluno: ");
                    String nomeAluno = scanner.nextLine();

                    int idadeAluno;
                    System.out.print("Idade (maior que 0): ");
                    do {
                        idadeAluno = scanner.nextInt();
                        if (idadeAluno <= 0) {
                            System.out.println("[AVISO] Idade invalida. Digite um valor maior que 0.");
                        }
                    } while (idadeAluno <=0);

                    String matricula    ;
                    boolean matriculaDuplicada;
                    System.out.print("Matrícula: ");
                    do {
                        matricula = scanner.nextLine().trim(); // Impede a matricula de ser pulada por algum motivo
                        if (matricula.isEmpty()) {
                            matriculaDuplicada = true;
                            continue;
                        }
                        matriculaDuplicada = false;
                        for (int i = 0; i < totalAlunos; i++) {
                            if (alunos[i].getMatricula().equalsIgnoreCase(matricula)) {
                                System.out.println("Matrícula já cadastrada! Digite uma matrícula diferente.");
                                matriculaDuplicada = true;
                                break;
                            }
                        }
                    } while (matriculaDuplicada);


                    double nota;
                    System.out.print("Nota (Entre 0 e 10): ");
                    do {
                        nota = scanner.nextInt();
                        if (nota < 0 || nota > 10) {
                            System.out.println("[AVISO] Nota invalida. Digite um valor entre 0 e 10.");
                        }
                    } while (nota <=0 || nota > 10);


                    alunos[totalAlunos] = new Aluno(nomeAluno, idadeAluno, matricula, nota);
                    totalAlunos++;
                    System.out.println("Aluno cadastrado com sucesso");
                    break;

                case 2:
                    System.out.println("-> Cadastrar professor");
                    if (totalProfessores >= professores.length) {
                        System.out.println("[ERRO] Limite de professores atingido");
                        break;
                    }

                    System.out.print("Nome do professor: ");
                    String nomeProf = scanner.nextLine();

                    int idadeProf;
                    System.out.print("Idade (maior que 0): ");
                    do {
                        idadeProf = scanner.nextInt();
                        if (idadeProf <= 0) {
                            System.out.println("[AVISO] Idade invalida. Digite um valor maior que 0.");
                        }
                    } while (idadeProf <=0);

                    scanner.nextLine();
                    System.out.print("Disciplina: ");
                    String disciplina = scanner.nextLine();

                    System.out.print("Salário mensal (maior que 0): R$ ");
                    Double salario;
                    do {
                        salario = scanner.nextDouble();
                        if (salario <= 0) {
                            System.out.println("[AVISO] Salário invalido. Digite um valor maior que 0.");
                        }
                    } while (salario <=0);
                    scanner.nextLine();

                    professores[totalProfessores] = new Professor(nomeProf, idadeProf, disciplina, salario);
                    totalProfessores++;
                    System.out.println("Professor cadastrado com sucesso");
                    break;

                case 3:
                    System.out.println("-> Lista de Alunos");
                    if (totalAlunos == 0) {
                        System.out.println("Nenhum aluno cadastrado.");
                    }else{
                        for (int i = 0; i < totalAlunos; i++) {
                            System.out.println("\n--- Aluno " + (i + 1) + " ---");
                            alunos[i].exibirDados();
                            alunos[i].verificarAprovacao();
                        }
                    }

                    break;

                case 4:
                    System.out.println("-> Lista de Professores");
                    if (totalProfessores == 0) {
                        System.out.println("Nenhum professor cadastrado.");
                    }else{
                        for (int i = 0; i < totalProfessores; i++) {
                            System.out.println("\n--- Professor " + (i + 1) + " ---");
                            professores[i].exibirDados();
                        }
                    }
                    break;

                case 5:
                if (totalAlunos == 0) {
                    System.out.println("[ERRO] Nenhum aluno cadastrado");
                    continue;
                }
                System.out.println("Digite o nome do aluno:");
                String buscaAluno = scanner.nextLine().trim().toLowerCase();
                boolean encontrouAluno = false;
                for (int i = 0; i < totalAlunos; i++) {
                    if (alunos[i].getNome().equalsIgnoreCase(buscaAluno)) {
                        System.out.println("\n--- Aluno encontrado ---");
                        alunos[i].exibirDados();
                        alunos[i].verificarAprovacao();
                        encontrouAluno = true;
                    }
                }
                if (!encontrouAluno) {
                    System.out.println("[ERRO] Aluno não encontrado");
                }
                    break;

                case 6:
                if (totalProfessores == 0) {
                    System.out.println("[ERRO] Nenhum professor cadastrado");
                    continue;
                }
                System.out.println("Digite o nome do professor:");
                String buscaProfessor = scanner.nextLine().trim().toLowerCase();
                boolean encontrouProfessor = false;
                for (int i = 0; i < totalAlunos; i++) {
                    if (professores[i].getNome().equalsIgnoreCase(buscaProfessor)) {
                        System.out.println("\n--- Professor encontrado ---");
                        professores[i].exibirDados();
                        encontrouProfessor = true;
                    }
                }
                if (!encontrouProfessor) {
                    System.out.println("[ERRO] Professor não encontrado");
                }
                    break;
                case 7:
                    System.out.println("-> Exibir dados completos");
                    System.out.println("--- Alunos ---");
                    if (totalAlunos == 0) {
                        System.out.println("Nenhum aluno cadastrado.");
                    }else{
                        for (int i = 0; i < totalAlunos; i++) {
                            System.out.println("\n--- Aluno " + (i + 1) + " ---");
                            alunos[i].exibirDados();
                            alunos[i].verificarAprovacao();
                        }
                    }
                    System.out.println("\n--- Professores ---");
                    if (totalProfessores == 0) {
                        System.out.println("Nenhum professor cadastrado.");
                    }else{
                        for (int i = 0; i < totalProfessores; i++) {
                            System.out.println("\n--- Professor " + (i + 1) + " ---");
                            professores[i].exibirDados();
                        }
                    }

                case 8:
                    System.out.println("Encerrando o sistema. Até logo!");
                    break;

                default:
                    System.out.println("Opção inválida. Tente novamente.");
            }

        } while (opcao != 0);

        scanner.close();
    }
}

//Questões no código

//• Para que serve extends: Permite uma Subclasse herdar características de uma Superclasse
//• Para que serve super: Chama métodos e construtores da Superclasse
//• Qual a vantagem da herança: Permite a criação de novas classes a partir de outras clases
//• Qual a diferença entre classe e objeto: A classe é como se fosse uma planta, 
// algo abstrato, enquanto o objeto é feito a partir de algo real, concreto
//• Qual a função dos métodos get e set: O método get retorna o valor de um atributo, 
// enquanto o método set define e altera esse mesmo atributo.