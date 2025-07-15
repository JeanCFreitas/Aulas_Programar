const lista = [
    {nome: 'Camiseta', preço: 50, imposto:10},
    {nome: 'Calça', preço: 100, imposto:15},
    {nome: 'Tênis', preço: 200, imposto:20}
]

const final = lista.map(function(lista){
    return lista.preço + lista.imposto;
})

