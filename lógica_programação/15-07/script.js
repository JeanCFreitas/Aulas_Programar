//criando uma classe
class Carro {
    constructor(marca, modelo, ano){
        this.marca=marca;
        this.modelo=modelo;
        this.ano=ano;
    }
    //criando o método detalhes carro
    detalhesDoCarro(){
        return `Carro: ${this.modelo} ${this.marca}, 
        Ano: ${this.ano}`;
    }
}
//Criando meu objeto
const meuCarro = new Carro('Toyota', 'Corolla', 2022);

//Exibindo o resultado
console.log(meuCarro.detalhesDoCarro())