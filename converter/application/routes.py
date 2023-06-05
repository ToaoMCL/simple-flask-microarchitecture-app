from flask import Flask
from application import app


@app.route('/converter/<convert>', methods=['GET', 'POST'])
def converter(convert):
    try:
        convert = int(float(convert))
    except ValueError:
        return "ValueError: enter a number"
    convertedCurrency = 1 * 1.25
    if convert < 1:
        return 'value entered is less than one'
    else: 
        return str(convertedCurrency)
    