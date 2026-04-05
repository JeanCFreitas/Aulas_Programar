import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;
public class Atividade1 {

    //Numero maximo de alunos
    static final int MAX_ALUNOS = 30;

    // Arrays paralelos para armazenar os dados dos alunos
    static String[] nomes = new String[MAX_ALUNOS];
    static double[] notas1 = new double[MAX_ALUNOS];
    static double[] notas2 = new double[MAX_ALUNOS];
    static double[] medias = new double[MAX_ALUNOS];
    static String[] situacoes = new String[MAX_ALUNOS];
    static String[] datasCadastro = new String[MAX_ALUNOS];

    // Contador de alunos cadastrados (tipo primitivo int)
    static int totalAlunos = 0;

    public static void main(String[] args){
    Scanner scanner = new Scanner(System.in);
    String entrada = "";

    // O loop continua enquanto a entrada for diferente de "sair"
    while (!entrada.equalsIgnoreCase("sair")) {
        System.out.println("Deseja Cadastrar ou Consultar alunos?");
        System.out.println("Digite 1 para Cadastrar ou 2 para Consultar");
        int decisao = -1;
        String opcaoStr = scanner.nextLine().trim();
        if (opcaoStr.isEmpty()) {
            continue;
        }
        try {
            decisao = Integer.parseInt(opcaoStr);
        } catch (NumberFormatException e) {
            System.out.println("Valor invalido");
            continue;
        }
        if (decisao == 1){

            
            if (totalAlunos >= MAX_ALUNOS) {
                System.out.println("Erro: Limite de " + MAX_ALUNOS + " alunos atingido.\n");
                return;
            } else {
                System.out.println("Existem " + totalAlunos + " Alunos cadastrados");
            }

            //Armazena nome do aluno
            System.out.println("Digite o nome do aluno:");
            String nomeDigitado = scanner.nextLine().trim().toLowerCase();
                
                // Percorre cada caractere e capitaliza a primeira letra de cada palavra
            String nome = "";
            boolean proximaMaiuscula = true;

            for (int i = 0; i < nomeDigitado.length(); i++) {
                char c = nomeDigitado.charAt(i);

                if (c == ' ') {
                    // Espaço: mantém e sinaliza que a próxima letra vira maiúscula
                    nome += c;
                    proximaMaiuscula = true;
                } else if (proximaMaiuscula) {
                    // Primeira letra da palavra: converte para maiúscula
                    nome += Character.toUpperCase(c);
                    proximaMaiuscula = false;
                } else {
                    // Demais letras: mantém minúscula
                    nome += c;
                }
            }

            //Armazena Notas 1 e 2 do aluno
            double nota1 = -1;
            System.out.println("Digite a primeira nota (0-10): ");
            do {
                nota1 = Double.parseDouble(scanner.nextLine().trim());
                if (nota1 < 0 || nota1 > 10) {
                    System.out.println("[AVISO] Nota invalida. Digite um valor entre 0 e 10.");
                }
            } while (nota1 < 0 || nota1 > 10);
            double nota2 = -1;
            System.out.println("Digite a segunda nota (0-10): ");
            do {
                nota2 = Double.parseDouble(scanner.nextLine().trim());
                if (nota2 < 0 || nota2 > 10) {
                    System.out.println("[AVISO] Nota invalida. Digite um valor entre 0 e 10.");
                }
            } while (nota2 < 0 || nota2 > 10);
        
            // Estrutura de controle: Cálculo da média
            double media = (nota1 + nota2) / 2;
            String status = "";
            if (media >= 6) {
                status = "Aprovado";
            } else{
                status = "Reprovado";
            }

            //Armaze
            LocalDateTime agora = LocalDateTime.now();
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");
            String dataCadastro = agora.format(formatter);

            //Armazena as informações do aluno em arrays
            nomes[totalAlunos]         = nome;
            notas1[totalAlunos]        = nota1;
            notas2[totalAlunos]        = nota2;
            medias[totalAlunos]        = media;
            situacoes[totalAlunos]     = status;
            datasCadastro[totalAlunos] = dataCadastro;
        
            // Saída com System.out.println
            System.out.println("--- CADASTRO REALIZADO ---");
            System.out.println("Aluno: " + nome);
            System.out.println("Nota 1: " + nota1);
            System.out.println("Nota 2: " + nota2);
            System.out.println("Media: " + media);
            System.out.println("Status: " + status);
            System.out.println("Data: " + dataCadastro);

            //Incrementa o contador de alunos
            totalAlunos += 1; 
    
        } else if (decisao == 2){
            if (totalAlunos == 0) {
                System.out.println("Erro: Nenhum aluno cadastrado ainda.\n");
            } else {

                //Mostra os alunos cadastrados e suas notas, média, situação e dia de cadastro
                System.out.println("\n--- LISTA DE ALUNOS CADASTRADOS ---");
                System.out.printf("%-4s %-20s %-7s %-7s %-7s %-12s %-20s%n",
                    "#", "Nome", "Nota1", "Nota2", "Media", "Situacao", "Cadastrado em");
                for (int i = 0; i < totalAlunos; i++) {
                    System.out.printf("%-4d %-20s %-7.1f %-7.1f %-7.1f %-12s %-20s%n",
                        (i + 1),
                        nomes[i],
                        notas1[i],
                        notas2[i],
                        medias[i],
                        situacoes[i],
                        datasCadastro[i]);
                }
            }
        } else {
            System.out.println("Valor invalido");
        }

        System.out.println("Digite 'sair' para sair ou 'continuar' para continuar");
        entrada = scanner.nextLine().trim(); // Decide se acaba ou não o sistema.
    }
    

    System.out.println("Programa encerrado.");
    scanner.close();
    }
}