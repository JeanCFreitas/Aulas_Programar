
from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)

@app.route('/user/<username>')
def profile(username):
    return render_template('profile.html', user=username)

@app.route('/')        
def home():
    produtos=["Maçã","Banana","Laranja"]
    logado=True
    return render_template("home.html", produtos=produtos, logado=logado)

app.secret_key = 'Uma-chave-secreta-muito-segura-e-dificil-de-adivinhar'
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    session['username'] = username
    return redirect(url_for('profile'))

if __name__=='__main__':
    app.run(debug=True)