from flask import Flask, render_template, Markup, request, flash
from flask_inputs import Inputs
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import DataRequired

import pandas as pd
import csv
import urllib2

app = Flask(__name__)
app.secret_key = 'EPPbPMgMm5uZ' #haha not so secret!

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/test1', methods=['GET'])
def testText():
	#txt = request.form['lb2']
	txt=request.args.get('lb2')
	txt=[txt]
	return render_template('test1.html', title='ExerTest', text=txt)
