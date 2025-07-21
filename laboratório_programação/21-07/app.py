#flask --app app run
#^ Roda o código

#pip install --proxy http://proxy.spo.ifsp.edu.br:3128 flask
#Baixa flask no pc escola

from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'
login = None


@app.route("/")
def hello_world():
    return "<center><h1>Olá, Mundo!</h1></center>"

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form")
def form():
    return render_template("formulario.html")

@app.route("/cadastrar_usuario", methods=['POST', 'GET'])
def cadastro():
    global login
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not email or not password:
            flash('Todos os campos são obrigatórios!', 'danger')
            return render_template('formulario.html')
        else:
            if login is None:
                login=[username, email, password]
                flash(f'Usuário {username} cadastrado!', 'success')
                return render_template('formulario.html')
            else:
                
                if username == login[0] and email == login[1] and password == login[2]:
                    flash(f'Bem-vindo(a) devolta, {username}.', 'success')
                    return render_template('formulario.html')
                else:
                    flash('Login falhou. Verifique seus dados.', 'danger')
                    return render_template('formulario.html')
        
        
    return username

if __name__ == "__main__":
    app.run(debug=True)