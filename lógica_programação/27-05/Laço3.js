//Validação de sexo

//Criação o laço do...while
do{
    let texto = "Feminino";
    sexo = texto.charAt(0);

    if(sexo!='F'&& sexo!='M')
        console.log("Enby")

}while (sexo != 'F' && sexo != 'M')

console.log("Sexo confirmado")