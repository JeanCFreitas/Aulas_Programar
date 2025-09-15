from flask import Flask, render_template, request, redirect, url_for
from models import UsuarioModel
#flask --app app run
#^ Roda o código

#pip install --proxy http://proxy.spo.ifsp.edu.br:3128 flask
#^ Baixa Flask no pc da escola
app = Flask(__name__)
usuario_model = UsuarioModel()

@app.route('/usuarios')
def listar_usuarios():
    usuarios = usuario_model.get_todos()
    return render_template('usuarios.html', lista_de_usuarios = usuarios)

@app.route('/usuarios/novo', methods=['POST'])
def adicionar_usuario():
    nome = request.form['nome']
    email = request.form['email']
    usuario_model.salvar(nome,email)
    return redirect(url_for('listar_usuarios'))



if __name__=='__main__':
    app.run(debug=True) 