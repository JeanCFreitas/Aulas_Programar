
const soma = function(a, b) {return a+b}
const sub = function(a, b) {return a-b}
const mult = function(a, b) {return a*b}
const div = function(a, b) {return a/b}


while (true){
    let operacao, a=15, b=3
    console.log("Calculadora\n")
    console.log("adicao/subtracao/multiplicacao/divisao")
    operacao = 1
    switch (operacao){
        case 1:
            console.log("a soma entre " + a + " e " + b + " é " + soma(a, b))
        case 2:
            console.log("a soma entre " + a + " e " + b + " é " + sub(a, b))
        case 3:
            console.log("a soma entre " + a + " e " + b + " é " + mult(a, b))
        case 4:
            console.log("a soma entre " + a + " e " + b + " é " + div(a, b))
    }
}

