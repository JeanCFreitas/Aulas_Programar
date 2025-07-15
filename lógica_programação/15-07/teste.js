const num = [432, 1235, 6344, 1230, 123];
const resultimpar = num.filter(impar);
console.log(resultimpar)
function impar(num) {
return num%2!=0;
}
