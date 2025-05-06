var idade = 67;
var A = "Não-eleitor (abaixo de 16 anos)";
var B = "Eleitor obrigatório (entre 18 e 65 anos)";
var C = "Eleitor facultativo (entre 16 e 18 e maior de 65 anos)";
if ((idade > 16) && (idade > 65)) {
  console.log(C);
}
if ((idade < 65) && (idade > 18)) {
  console.log(B);
}
if (idade < 16) {
  console.log(A);
}
