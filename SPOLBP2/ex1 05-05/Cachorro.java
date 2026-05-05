package EX1;

public class Cachorro extends Animal {
    public Cachorro(String nome, Integer idade){
        super( nome, idade);
    };
    public void emitirSom(){
        System.out.println("auau");
    }
      
}