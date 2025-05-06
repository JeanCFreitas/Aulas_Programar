let TEMPO = 3;
const VELOCIDADE = 80;
let DISTÂNCIA = TEMPO * VELOCIDADE;
let LITROS_USADOS = DISTÂNCIA / 12;

console.log('O tempo foi ' + TEMPO + ' horas');
console.log('A velocidade média foi de ' + VELOCIDADE + 'kms/h');
console.log('A distância percorrida foi de ' + DISTÂNCIA + 'kms');
console.log('Foi gasto ' + LITROS_USADOS + ' litros de gasolina');