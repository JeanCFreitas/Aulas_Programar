from flask import Flask, render_template, jsonify

#flask --app app run
#^ Roda o código

#pip install --proxy http://proxy.spo.ifsp.edu.br:3128 flask
#^ Baixa Flask no pc da escola

# Rota 1: Serve a "casca" da aplicação (o HTML vazio)
app = Flask(__name__)

# Rota para servir a página principal
@app.route("/")
def index():
    return render_template("index.html")

# API que retorna dados em JSON
@app.route("/api/data")
def get_data():
    dados = [
        {"id": 1, "nome": "Mesa", "descricao": "Conheça mesas bonitas para suas salas" ,"img": "https://cdn.vnda.com.br/800x/industrialmoveis/2023/03/01/10_10_39_193_387e4e5249e1e04188d0c0d2e10b4472.jpg?v=1677676239"},
        {"id": 2, "nome": "Cadeira", "descricao": "Temos cadeiras boas para salas, cozinhas e escritórios" ,"img": "https://cdn.awsli.com.br/2500x2500/1804/1804030/produto/88478931/cadeira-de-jantar-em-madeira-maci-a-larissa-4gnkv8r94b.jpg"},
        {"id": 3, "nome": "Almofada", "descricao": "Almofadas bonitas para suas camas e sofas" ,"img": "https://images.yampi.me/assets/stores/bordabordados/uploads/images/almofada-liz-tricot-tranca-50cm-x-50cm-01-peca-azul-jeans-672e71654b859-medium.jpg"}
    ]
    return jsonify(dados)

if __name__ == "__main__":
    app.run(debug=True)