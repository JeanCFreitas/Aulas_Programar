var a = 9;
var b = 3.7;
var c = 2;
var d = 8.5;
var A = a + b + (a * b) + a + c + (a * c) + a + d + (a * d);
var B = b + c + (b * c) + b + d + (b * d);
var C = c + d + (c * d);
console.log('Resultado = ' + (A + B + C));