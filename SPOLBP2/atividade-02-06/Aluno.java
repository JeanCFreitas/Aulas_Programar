public class Aluno extends Pessoa {

    private String matricula;
    private Double nota;

    public Aluno() {

    }
    public Aluno(String nome, Integer idade, String matricula, Double nota) {
        super( nome, idade );
        this.matricula = matricula;
        this.nota = nota;
    }

    public String getMatricula(){
        return matricula;
    }
    public void setMatricula(String matricula){
        this.matricula = matricula;
    }

    public Double getNota(){
        return nota;
    }
    public void setIdade(Double nota){
        this.nota = nota;
    }

    public void verificarAprovacao(){
        if (nota>=6){
            System.out.println("Aluno aprovado");
        }else{
            System.out.println("Aluno reprovado");
        }
    }

    @Override
    public void exibirDados() {
        super.exibirDados();
        System.out.println("Matrícula: " + matricula);
        System.out.printf("Nota: %.1f%n", nota);
    }
}