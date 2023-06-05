from flask import Flask
from application import app
import requests
from flask import render_template, request, redirect, url_for
import sys



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    formData = request.form.get('currency')
    formData = int(float(formData))
    money = requests.post('http://converter:5001/convert/' + formData)
    return render_template('convertPrime.html', formData=formData, birthDate=money.text)
