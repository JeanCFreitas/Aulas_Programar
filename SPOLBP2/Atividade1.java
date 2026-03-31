import java.util.Scanner;
public class Atividade1 {
   public static void main(String[] args){
    Scanner scanner = new Scanner(System.in);
    String entrada = "";

    // O loop continua enquanto a entrada for diferente de "sair"
    while (!entrada.equalsIgnoreCase("sair")) {
        System.out.println("Deseja Cadastrar ou Consultar alunos?");
        System.out.println("Digite 1 para Cadastrar ou 2 para Consultar");
        int decisao = scanner.nextInt();
        if (decisao == 1){

            System.out.println("Digite o nome do aluno: ");
            String nome = scanner.next();
        
            System.out.println("Digite a primeira nota (0-10): ");
            double nota1 = scanner.nextDouble();
        
            System.out.println("Digite a segunda nota (0-10): ");
            double nota2 = scanner.nextDouble();
        
            // Estrutura de controle: Cálculo da média
            double media = (nota1 + nota2) / 2;
        
            // Saída com System.out.println
            System.out.println("--- Resultado ---");
            System.out.println("Aluno: " + nome);
            System.out.println("Média: " + media);
            
    
        } else if (decisao == 2){
            System.out.println("placeholder");
        } else {
            System.out.println("Valor invalido");
        }

        System.out.println("Digite 'sair' para sair ou 'continuar' para continuar");
        entrada = scanner.next(); // Lê a entrada do usuário
    }
    

    System.out.println("Programa encerrado.");
    scanner.close();
    }
}
