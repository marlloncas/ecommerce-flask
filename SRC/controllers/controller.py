
from flask.views import MethodView
from flask import request, render_template, redirect
from src.db import pymysql

class OlaController(MethodView):
    def get(self):
        return render_template('public/index.html')
    
    def post(self):
        ID_CUPOM = request.form['ID_CUPOM']
        NOME = request.form['NOME']
        VALOR_DESCONTO = request.form['VALOR_DESCONTO']

        print(ID_CUPOM,NOME, ID_CUPOM)
        return "CUPOM CADASTRADO COM SUCESSO!"