//trabalhando com Array e laço de repetição do while
const alunos = [
    {aluno: "Henrique", nota: 8},
    {aluno: "Jao", nota: 10},
    {aluno: "Bea", nota: 9},
    {aluno: "Gui", nota: 7}
]
let index = 0
let somanotas = 0
let totalalunos = alunos.length

//utilizando o laço de repetição
do{
    somanotas+=alunos[index].nota
    ++index
}while (index < totalalunos)

let media = somanotas / totalalunos

console.log(media)