document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('registrationForm');
    const mensagens = document.getElementById('mensagens');
  
    form.addEventListener('submit', function (event) {
      event.preventDefault();
  
      const username = document.getElementById('username');
      const password = document.getElementById('password');
      const email = document.getElementById('email');
  
      let erros = [];
  
      if (username.value.trim() === '') {
        erros.push('O campo Usuário é obrigatório.');
      }
  
      if (password.value.trim() === '') {
        erros.push('O campo Senha é obrigatório.');
      }
  
      if (email.value.trim() === '') {
        erros.push('O campo Email é obrigatório.');
      } else {
        const emailValido = /^[^[^@]\.[^\s@]+/;
        if (!emailValido.test(email.value.trim())) {
          erros.push('O formato do email está incorreto.');
        }
      }
  
      if (erros.length > 0) {
        mensagens.innerHTML = erros.map(erro => `<p>${erro}</p>`).join('');
      } else {
        mensagens.innerHTML = '<p style="color: green;">Cadastro realizado com sucesso!</p>';
        form.submit();
      }
    });
  });
  