# app.py (versão corrigida e comentada)

from flask import Flask, render_template, jsonify

#flask --app app run
#^ Roda o código

#pip install --proxy http://proxy.spo.ifsp.edu.br:3128 flask
#^ Baixa Flask no pc da escola

app = Flask(__name__)
# Nossos dados continuam os mesmos
dados_biografias = {
    "santos_dumont":{
        "nome": "Stantos Dumont",
        "texto": "Alberto Santos de Dumont foi um aeronauta, esportista e inventor brasileiro..."
    },
    "marie_curie":{
        "nome": "Marie Curie",
        "texto": "Marie Sklodowska Curie foi uma física e química polonesa naturalizada francesa..."
    },
    "eintein":{
        "nome": "Albert Einstein",
        "texto": "Albert Einstein foi um físico teórico alemão que desenvolveu a teoria da relatividade gera..."
    }
}

@app.route("/")
def index():
    personagens = dados_biografias.keys()
    return render_template("index.html", personagens=personagens, nomes=dados_biografias)

# esta rota deve retornar os dados em formato JSON usando jsonify
@app.route("/biografia/<id_personagem>")
def get_biografia(id_personagem):
    """
    Busca os dados do personagem no nosso dicionário.
    Usa .get() para retornar um valor padrão caso o id não seja encontrado, evitando erros;
    """
    biografia_dat = dados_biografias.get(id_personagem, {
        "nome": "Desconhecido",
        "texto": "Personagem não encontrado."
    })
    # jsonify é a forma correta de retornar um dicionário como resposta de API
    # ele garante que o navegador entenderá que está recebendo dados JSON.
    return jsonify(biografia_dat)

if __name__ == "__main__":
    app.run(debug=True)