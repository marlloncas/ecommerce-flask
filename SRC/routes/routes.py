#Importação da página default da pasta controllers.
from src.controllers.controller import *
from src.controllers.erros import NotFoundController

#criação da rota passando o nome e importando a classe da controller
routes = {    
    "ola_mundo": "/","olamundo": OlaController.as_view("ola"),
    #Nome definido para a rota/Definição do erro 404/Nome da classe/Nome da classe
    "not_found_route":404,"not_found_controller": NotFoundController.as_view("not_found"),
}