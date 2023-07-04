#IMPORTAÇÃO DO FLASK
from flask import Flask

#importação da ROUTES
from src.routes.routes import *

#Instância da classe app
app = Flask(__name__)

#instância da da router em uma nova regra de urls passando como parâmentro um discionario [Chave:valor]
app.add_url_rule(routes["ola_mundo"],view_func=routes["olamundo"] )

#Rota da mensagem de erro de registro no db.
app.register_error_handler(routes["not_found_route"], routes["not_found_controller"])