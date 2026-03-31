function buscarCep() {
    let cep = document.getElementById('cep').value.replace(/\D/g, '');
    if (cep !== "" && cep.length === 8) {
        fetch(`https://viacep.com.br/ws/${cep}/json/`)
        .then(response => {
            if (!response.ok) throw new Error("Erro na rede");
            return response.json(); // Converte a resposta para um objeto JavaScript
            })
            .then(data => {
                
                    document.getElementById('rua').innerText = data.logradouro;
                    document.getElementById('bairro').innerText = data.bairro;
                    document.getElementById('cidade').innerText = data.localidade;
                    document.getElementById('estado').innerText = data.estado;
                
            })
            .catch(erro => {
                console.error("Houve um problema com a requisição:", erro);
        });
    }
}