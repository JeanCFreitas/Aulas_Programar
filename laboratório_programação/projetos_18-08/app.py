from flask import Flask, render_template, request, flash, redirect, url_for

#flask --app app run
#^ Roda o código

#pip install --proxy http://proxy.spo.ifsp.edu.br:3128 flask
#^ Baixa Flask no pc da escola

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('catálogo.html',)

@app.route('/noticias')
def noticias():
    username = request.cookies.get('username')
    return render_template('noticias.html', user=username)

if __name__ == '__main__':
    app.run(debug=True)