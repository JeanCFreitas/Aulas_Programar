//criando uma função anonima
const imprimirsoma = function(a,b){
    console.log(a+b)
}

imprimirsoma(2,3)

//criando a minha função de seta
const soma = (a,b) =>{
    return (a+b)
}

//exibindo valor
console.log(soma(2,3))

//retorno implícito
const subtracao = (a,b) => a-b
console.log(subtracao(2,3))

const imprime2 = a => console.log(a)
imprime2('Legal!')