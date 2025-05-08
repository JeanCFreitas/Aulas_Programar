let prova1 = 4;
let prova2 = 3;
let tr = 3;
let media = [(prova1 * 0.4) + (prova2 * 0.6)] * 0.7 + tr;
let faltas = 18;
if (media >= 6 && faltas < 24) {
  console.log('Aluno aprovado! média é ' + media);
}
if (media >= 3 && media < 6) {
  console.log('Aluno de exame! média é ' + media);
} else {
  console.log('Aluno reprovado!');
}
if (faltas >= 24) {
  console.log('Aluno reprovado por faltas: ' + faltas + ' faltas');
}