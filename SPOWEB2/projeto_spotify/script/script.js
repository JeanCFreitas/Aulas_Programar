//Criando variável constante para pegar o Id do botão
const botaoAproveite = document.getElementById("aproveite");
const numero = 5;

//Criando o Evento que ficará esperando a função de clique do mouse
botaoAproveite.addEventListener("click", this.variosAlertas);

//Função que é chamada para fazer algo
function alerta() {
    alert("Função Indisponível no Momento!");
    console.log(numero * numero);
}

function variosAlertas(){
    for(var i = 1; i <= 10; i++){
        alert("Inicializando no: " + i);
        console.log(i);
    }
}