from flask import render_template
from flask_app import app
from db_functions import getDataFromDatabase


@app.route('/')
@app.route('/index')

def index():

    rows = getDataFromDatabase()

    return render_template('index.html',rows=rows)