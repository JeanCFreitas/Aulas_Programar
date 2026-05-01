// Variáveis
const tarefaInput       = document.getElementById("tarefa");
const adicionarBotao    = document.getElementById("adicionar");
const listaTarefas      = document.getElementById("tarefas");
// CORRIGIDO: referencia o novo id único da lista de concluídas
const listaConcluidas   = document.getElementById("tarefas-concluidas");


// Event Listeners
adicionarBotao.addEventListener("click", adicionarTarefa);
tarefaInput.addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        adicionarTarefa();
    }
});


// Funções
function adicionarTarefa() {
    const tarefaTexto = tarefaInput.value;
    if (tarefaTexto.trim() !== "") {
        const novaTarefa = document.createElement("li");
        // ADICIONADO: botão "Concluída" junto ao botão "Excluir"
        novaTarefa.innerHTML = `
            <span class="tarefa-texto">${tarefaTexto}</span>
            <div class="botoes">
                <button class="concluir">Concluída</button>
                <button class="excluir">Excluir</button>
            </div>
        `;
        listaTarefas.appendChild(novaTarefa);
        tarefaInput.value = "";
    }
}


// Delegação de eventos na lista de tarefas ativas
listaTarefas.addEventListener("click", function (e) {

    // Excluir tarefa ativa
    if (e.target.classList.contains("excluir")) {
        e.target.closest("li").remove();
    }

    // Mover tarefa para a lista de concluídas
    if (e.target.classList.contains("concluir")) {
        const item = e.target.closest("li");
        const texto = item.querySelector(".tarefa-texto").textContent;

        // Cria novo item na lista de concluídas com apenas o botão de excluir
        const itemConcluido = document.createElement("li");
        itemConcluido.classList.add("item-concluido");
        itemConcluido.innerHTML = `
            <span class="tarefa-texto">${texto}</span>
            <div class="botoes">
                <button class="excluir">Excluir</button>
            </div>
        `;
        listaConcluidas.appendChild(itemConcluido);

        // Remove da lista ativa
        item.remove();
    }
});


// Delegação de eventos na lista de concluídas (apenas excluir)
listaConcluidas.addEventListener("click", function (e) {
    if (e.target.classList.contains("excluir")) {
        e.target.closest("li").remove();
    }
});
