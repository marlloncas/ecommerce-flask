#IMPORTAÇÃO DO FLASK
from flask import Flask

#importação da ROUTES
from src.routes.routes import *


#Instância da classe app
app = Flask(__name__)

#instância da da router em uma nova regra de urls passando como parâmentro um discionario [Chave:valor]
app.add_url_rule(routes["ola_mundo"],view_func=routes["olamundo"] )