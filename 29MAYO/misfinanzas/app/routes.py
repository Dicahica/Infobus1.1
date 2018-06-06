from flask import render_template
from app import app, db, models, forms
from app.forms import LoginForm
from flask import render_template, flash, redirect,url_for, request
from app.forms import Formulario_Cuentas
from app.models import Tipo_Cuenta


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/dir')
def dir():
    return render_template('direccion.html')