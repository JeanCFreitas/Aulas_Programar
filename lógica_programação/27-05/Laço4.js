/*Utilizando o laço de repetição do...while, imprima o primeiro número divisível por 19*/
//leve em consideração o valor do primeiro numero 100 e do segundo número 200


let começo=100;
let fim=200;
do{
    if(começo % 19 == 0){
        console.log(começo)
        break
    }
    ++começo
}while (começo<fim)

