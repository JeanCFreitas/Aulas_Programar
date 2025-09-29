from flask import Flask, request
import logging

#configuração de logs
logging.basicConfig(level=logging.INFO)

#criação da instância da aplicação
app = Flask(__name__)
app.config['SECRET_KEY']='uma-chave-muito-dificil'

#middleware de log
@app.before_request
def log_request_info():
  app.logger.info('Requisição Recebida: %s %s', request.method, request.path)

#importa as rotas no final para evitar importação circular