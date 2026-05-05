package EX1;

public class Gato extends Animal {
    public Gato(String nome, Integer idade){
        super( nome, idade);
    };
    public void emitirSom(){
        System.out.println("Miau");
    }
      
}