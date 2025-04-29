let x=4, y=7;
if(x<y){
    x++;
    y--;
    if(x===y){
        console.log("Iguais");
    }else if (x>y){
        console.log("X maior")
    }else{
        console.log("Y maior")
    }
}else{
    console.log("X não é menor que Y")
}