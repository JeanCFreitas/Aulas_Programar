// 1. Definimos o "Banco de Dados" ou as "Views" das nossas páginas
const rotas = {
    '#home': '<h2>Página Inicial</h2><p>Bem-vindo à nossa primeira Single Page Application!</p>',
    '#sobre': '<h2>Sobre o Curso</h2><p>Estamos aprendendo os conceitos fundamentais de SPAs.</p>',
    '#contato': '<h2>Contato</h2><p>Fale com o professor: professor@ifsp.edu.br</p>'
    };
    const appDiv = document.getElementById('app');
    // 2. Criamos a função que atualiza o conteúdo da tela
    function navegar() {
    // Pega o hash atual da URL (ex: #sobre). Se não tiver, usa #home como padrão.
    let hashAtual = window.location.hash || '#home';
    // Injeta o HTML correspondente à rota dentro da div #app
    // Se o usuário digitar um hash que não existe, mostra erro 404
    appDiv.innerHTML = rotas[hashAtual] || '<h2>Erro 404</h2><p>Página não encontrada.</p>';
    }
    // 3. Adicionamos o "espião" que avisa quando a URL (hash) muda
    window.addEventListener('hashchange', navegar);
    // 4. Rodamos a função pela primeira vez quando a página carrega
    window.addEventListener('load', navegar);