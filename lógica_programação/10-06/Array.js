//Trabalhando com Array

const valores = [7.7,8.9,6.3,9.2]
console.log(valores[0], valores[3])
console.log(valores[4]) //nao existe

valores[4]=10
console.log(valores[4])


valores[10]=20
console.log(valores)

console.log(valores.length)

//inserido mais valores no Array
valores.push({id: 3}, false, null, 'test')
console.log(valores)

console.log(valores.pop())
delete valores
console.log(valores)

console.log(typeof valores)