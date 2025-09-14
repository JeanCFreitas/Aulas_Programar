document.getElementById("loadBtn").addEventListener("click", () => {
    fetch("/api/data")
        .then(response => response.json())
        .then(dados => {
            const container = document.getElementById("content");
            container.innerHTML = ""; // limpa antes de renderizar
            dados.forEach(item => {
                const card = document.createElement("div");
                card.className = "col-md-4";
                card.innerHTML = `
                    <div class="card shadow-sm p-3 text-center">
                        <div class="card-body">
                            <h5 class="card-title">${item.nome}</h5>
                            <p class="card-text">${item.descricao}</p>
                        </div>
                        <img src="${item.img}" class="card-img-top mx-auto" alt="${item.nome}" style="width:400px; height:400px; object-fit:contain;">
                    </div>
                `;
                container.appendChild(card);
            });
        })
        .catch(error => console.error("Erro ao carregar dados:", error));
});
