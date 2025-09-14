// Páginas do SPA
const pages = {
    mesas: `
        <h1>Mesas:</h1>
        <p>Conheça mesas bonitas para suas salas.</p>
        <img src="https://cdn.vnda.com.br/800x/industrialmoveis/2023/03/01/10_10_39_193_387e4e5249e1e04188d0c0d2e10b4472.jpg?v=1677676239" height="270">
    `,
    cadeiras: `
        <h1>Cadeiras:</h1>
        <p>Temos cadeiras boas para salas, cozinhas e escritórios.</p>
        <img src="https://cdn.awsli.com.br/2500x2500/1804/1804030/produto/88478931/cadeira-de-jantar-em-madeira-maci-a-larissa-4gnkv8r94b.jpg" height="270">
    `,
    almofadas: `
        <h1>Almofadas:</h1>
        <p>Almofadas bonitas para suas camas e sofas.</p>
        <img src="https://images.yampi.me/assets/stores/bordabordados/uploads/images/almofada-liz-tricot-tranca-50cm-x-50cm-01-peca-azul-jeans-672e71654b859-medium.jpg" height="270">
    `
};

// Função de navegação SPA
function navigate(page) {
    document.getElementById("content").innerHTML = pages[page] || "<h1>Clique nas opções de cima para ver nosso catálogo.</h1>";
}

// Carregar dados da API Flask
async function loadAPI() {
    const response = await fetch("/api/data");
    const data = await response.json();
    document.getElementById("api-result").innerHTML = `<p><b>Resposta:</b> ${data.message}</p>`;
}

// Carregar página inicial
window.onload = () => navigate("home");
