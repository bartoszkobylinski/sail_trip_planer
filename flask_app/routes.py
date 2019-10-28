from flask import render_template
from flask_app import app
from db_functions import get_data_from_database


@app.route('/')
@app.route('/index')

def index():

    rows = get_data_from_database()

    return render_template('index.html',rows=rows)