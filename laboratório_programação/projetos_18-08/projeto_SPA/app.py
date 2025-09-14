from flask import Flask, render_template, jsonify
#flask --app app run
#^ Roda o código

#pip install --proxy http://proxy.spo.ifsp.edu.br:3128 flask
#^ Baixa Flask no pc da escola
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/cadeiras")
def data():
    # Exemplo de dados retornados pela API
    return jsonify({"message": "Olá! Esses dados vieram do Flask 🚀"})

if __name__ == "__main__":
    app.run(debug=True)
