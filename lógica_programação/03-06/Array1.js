//tipos de Array
console.log(typeof Array)
console.log(typeof new Array)
console.log(typeof [])

//criar um  Array
let aprovados = new Array('Bia', 'Carlos', 'Ana');
console.log(aprovados)

//acessando cada elemento
console.log(aprovados[0])
console.log(aprovados[1])
console.log(aprovados[2])

//exibindo conteúdo que não existe no Array
console.log(aprovados[3])

//exibir conteúdo no índice 3
aprovados[3] = 'Fernando'
console.log(aprovados[3])

//inserir dado na última posição
aprovados.push('Abia')
console.log(aprovados)

//retornar tamanho Array
console.log(aprovados.length)

//incluindo dados fora do Array
aprovados[9] = 'Rafael'
console.log(aprovados)

//comparar undefined
console.log(aprovados[8]==undefined)

//comparar null
console.log(aprovados[8]==null)

//deletar conteúdo
delete aprovados[0]
console.log(aprovados)

//organizar em ordem alfabetica
aprovados.sort()
console.log(aprovados)

//criar um  Array
aprovados = ['Bia', 'Carlos', 'Ana'];
console.log(aprovados)
aprovados.splice(1,1)
-console.log(aprovados)