#Importação da página default da pasta controllers.
from src.controllers.controller import *

#criação da rota passando o nome e importando a classe da controller
routes = {
    "ola_mundo": "/","olamundo":OlaController.as_view("ola")
}