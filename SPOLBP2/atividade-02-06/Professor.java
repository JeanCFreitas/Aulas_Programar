public class Professor extends Pessoa {

    private String disciplina;
    private Double salario;

    public Professor() {
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

    public void calcularSalarioAnual(){

    }
}
