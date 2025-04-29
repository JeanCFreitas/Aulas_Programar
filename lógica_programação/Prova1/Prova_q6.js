let val = 1;

if (val<5){
    val +=2;
    if(val===3){
        val++;
        if(val<5){
            console.log("Menor que cinco");
        }else{
            console.log("Cinco")
        }
    }else{
        console.log("Não é três")
    }
}else{
    console.log("Maior/igual a cinco")
}