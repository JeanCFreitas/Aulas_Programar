from flask import Flask, render_template
#flask --app app run
#^ Roda o código

#pip install --proxy http://proxy.spo.ifsp.edu.br:3128 flask
#^ Baixa Flask no pc da escola
app = Flask(__name__)
@app.route('/')
def pagina_inicial():
   return render_template('index.html')
@app.route('/sobre')
def pagina_sobre():
   return render_template('sobre.html')
if __name__ == '__main__':
   app.run(debug=True, port=5002)