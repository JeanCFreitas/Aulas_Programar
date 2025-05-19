from flask import Flask
app = Flask('/bemvindo/pag')
@app.route('/')
def ola_mundo(nome):
    return render_template('pag.html', usuario=nome)