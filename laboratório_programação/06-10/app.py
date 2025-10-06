from flask import Flask, render_template, request, abort, jsonify
import math
app = Flask(__name__)

#flask --app app run
#^ Roda o código

#pip install --proxy http://proxy.spo.ifsp.edu.br:3128 flask
#^ Baixa Flask no pc da escola

#Nossa base de dados em memória
#uma lista de dicionarios
PRODUTOS=[
    {"id": 1, "nome": "Notebook Gamer X", "preco": 5200.00},
    {"id": 2, "nome": "Mouse sem fio", "preco": 150.00},
    {"id": 3, "nome": "Teclado Mecânico RGB", "preco": 350.00},
    {"id": 4, "nome": "Monitor 27 Polegadas", "preco": 1800.00}
]
@app.route('/produtos')
def listar_produtos():
    return render_template('produtos.html', produtos=PRODUTOS)

# (lista de PRODUTOS definida anteriormente)
@app.route('/produtos-paginados')
def listar_produtos_paginados():
  page = request.args.get('page', 1, type=int)
  per_page = 5 #itens por página

  #lógica da paginação
  start = (page - 1) * per_page
  end = start + per_page
  total_pages = math.ceil(len(PRODUTOS) / per_page)

  #fatiando a lista para pegar apenas os itens da página atual
  produtos_da_pagina = PRODUTOS[start:end]
  render_template('produtos_paginados.html', produtos=produtos_da_pagina, page=page, total_pages=total_pages)

#lista de PRODUTOS definida anteriormente
@app.route('/produto/<int:produto_id>')
def detalhe_produto(produto_id):
  produto_encontrado = None
  #busca pelo produto na lista (performance0(n))
  for produto in PRODUTOS:
    if produto["id"] == produto_id:
      produto_encontrado = produto
      break
    if produto_encontrado is None:
      abort(404) #item n encontrado
  return render_template('detalhe_produto.html', produto=produto_encontrado)

@app.errorhandler(404)
def pagina_nao_encontrada(error):
  return render_template('404.html'), 404

#lista de PRODUTOS
@app.route('/api/buscar-produto', methods=["POST"])
def buscar_produto():
  dados = request.get_json()
  nome_produto = dados.get('nome', '').lower()
  
  #busca na nossa lista de dicionarios
  resultado = [p for p in PRODUTOS if nome_produto in p['nome'].lower()]
  return jsonify({'produtos_encontrados': resultado})

if __name__=='__main__':
  app.run(debug=True)