
// Banco de Dados Simulado
const bancoDeJogos = [
{ id: 1, titulo: "Resident Evil 4 Remake", genero: "Terror/Ação", 
    preco: "R$ 199,00" },
{ id: 2, titulo: "Persona 3 Reload", genero: "RPG",
    preco: "R$ 349,00" },
{ id: 3, titulo: "EA Sports FC 24", genero: "Esporte",
    preco: "R$ 250,00" }
];
// Referência para a área principal da tela
const container = document.getElementById('conteudo');
// SUAS TAREFAS:
// 1. Crie uma função para gerar o HTML do catálogo percorrendo o array 'bancoDeJogos';
function navegar() {
// Pega o hash atual da URL (ex: #sobre). Se não tiver, usa #home como padrão.
    let hashAtual = window.location.hash || '#home';
// Injeta o HTML correspondente à rota dentro da div #app
// Se o usuário digitar um hash que não existe, mostra erro 404
        appDiv.innerHTML = rotas[hashAtual] || '<h2>Erro 404</h2><p>Página não encontrada.</p>';
}

// 2. Crie o objeto 'rotas' contendo o HTML de #home, do #catalogo e do #carrinho.
const rotas = {
  '#home': `
      <h1>Bem-vindo à SPO Games </h1>
      <p>Sua loja de jogos digitais com os melhores títulos do mercado.</p>
      <a href="#catalogo" class="btn-hero">Ver Catálogo</a>
  `,
   '#catalogo':`
      <h1>Catálogo de jogos disponíveis</h1>
      <p>Aqui está uma lista dos nossos jogos disponíveis.</p>
      <div class="catalogo-grid">
      ${bancoDeJogos.map(jogo => `
      <div class="jogo-card">
        <h3>${jogo.titulo}</h3>
        <span>${jogo.genero}</span>
        <span>${jogo.preco}</span>
      </div>
      `).join('')}
    </div> 
      <a href="#catalogo" class="btn-hero">Ver Catálogo</a>`,
   '#carrinho': `
      <div class="carrinho-vazio">
      <h1>Carrinho</h2>
      <p>Seu carrinho está vazio.</p>
      <a href="#catalogo" class="btn-hero">Ir ao Catálogo</a>
    </div>
  `,
}
// 3. Crie a função de navegação para ler o window.location.hash e injetar no 'container';
function navegar() {
  // Lê o hash atual; se estiver vazio, assume #home
  const hash = window.location.hash || '#home';

  // Atualiza o link ativo na navegação
  document.querySelectorAll('nav a').forEach(link => {
    link.classList.toggle('ativo', link.getAttribute('href') === hash);
  });

  // Verifica se a rota existe; caso contrário, exibe 404
  if (rotas[hash]) {
    container.innerHTML = rotas[hash];
  } else {
    container.innerHTML = `
        <div class="erro-404">
        <span class="erro-codigo">404</span>
        <h2>Rota não encontrada</h2>
        <p>A página <code>${hash}</code> não existe nesta aplicação.</p>
        <a href="#home" class="btn-hero">Voltar ao Início</a>
         </div>
    `;
  }
}
// 4. Adicione os Event Listeners necessários ('hashchange' e 'load');

window.addEventListener('hashchange', navegar);
window.addEventListener('load', navegar);