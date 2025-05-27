//Criando um menu

//criar uma váriavel
let opção='c';

//criando o menu
console.log("Escolha\n")
console.log("(s) - Solteiro")
console.log("(c) - Casado")
console.log("(d) - Divorciado\n\n")

//teste
switch(opção){
    case 's': console.log("Solteiro"); break
    case 'c': console.log("Casado"); break
    case 'd': console.log("Divorciado"); break
    default: console.log("Outros"); break
}