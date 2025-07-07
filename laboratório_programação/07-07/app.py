from flask import Flask, render_template, request, redirect, url_for,make_response

app = Flask(__name__)
sessao=0
USUARIO_CADASTRADO = "admin"
SENHA_CADASTRADA = "123"
pag=0
@app.route('/', methods=['GET', 'POST'])
def login():
    mensagem = ""
    if request.method == "POST":
        usuario = request.form['username']
        senha = request.form['password']
        if usuario == USUARIO_CADASTRADO and senha == SENHA_CADASTRADA:
            resposta = make_response(redirect(url_for('bemvindo')))
            resposta.set_cookie('username', usuario, max_age=60*10)
            return resposta
        if usuario != USUARIO_CADASTRADO or senha != SENHA_CADASTRADA:
            mensagem = "Usuário ou senha inválidos. Tente novamente."
        else:
            mensagem = "Usuário ou senha inválidos. Tente novamente."
    return render_template('login.html', error=mensagem)
@app.route('/bemvindo')
def bemvindo():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
    return render_template('bemvindo.html', user=username)
@app.route('/noticias')
def noticias():
    username = request.cookies.get('username')
    return render_template('noticias.html', user=username)
@app.route('/noticias/esportes')
def esportes():
    username = request.cookies.get('username')
    pag == 1
    return render_template('esportes.html', user=username)
@app.route('/noticias/entreterimento')
def entreterimento():
    username = request.cookies.get('username')
    pag==2
    return render_template('entreterimento.html', user=username)
@app.route('/noticias/lazer')
def lazer():
    username = request.cookies.get('username')
    pag==3
    return render_template('lazer.html', user=username)
if __name__ == '__main__':
    app.run(debug=True)