public class Professor extends Pessoa {

    private String disciplina;
    private Double salario;

    public Professor() {
        super();
    }
    public Professor(String nome, Integer idade, String disciplina, Double salario) {
        super( nome, idade );
        this.disciplina = disciplina;
        this.salario = salario;
    }

    public String getDisciplina(){
        return disciplina;
    }
    public void setDisciplina(String disciplina){
        this.disciplina = disciplina;
    }

    public Double getSalario(){
        return salario;
    }
    public void setSalario(Double salario){
        this.salario = salario;
    }

    public Double calcularSalarioAnual() {
        return salario * 12;
    }

    @Override
    public void exibirDados() {
        super.exibirDados();
        System.out.println("Disciplina: " + disciplina);
        System.out.printf("Salário Mensal: R$ %.2f%n", salario);
        System.out.printf("Salário Anual:  R$ %.2f%n", calcularSalarioAnual());
    }
}
