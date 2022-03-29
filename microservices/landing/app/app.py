from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import Api, Resource

import requests
import os

app = Flask(__name__)
#api = Api(app)
app.secret_key = 'thisisjustarandomstring'

@app.route('/', methods=['POST', 'GET'])
def index():
    if(request.form!={}):
         
        number_1 = request.form.get("first")
        number_2 = request.form.get('second')
        if number_1.isnumeric() and number_2.isnumeric():
            number_1=int(number_1)
            number_2=int(number_2)
        else:
            flash(f'Enter valid Input...')
            return render_template('index.html')
        operation = request.form.get('operation')
        result = 0
        if operation == 'add':
            res = requests.get("http://add-service:5051/{}/{}".format(number_1,number_2)).json()
  
        elif operation == 'minus':
            res = requests.get("http://sub-service:5052/{}/{}".format(number_1,number_2)).json()
            
        elif operation == 'multiply':
            res = requests.get("http://mul-service:5053/{}/{}".format(number_1,number_2)).json()
            
        elif operation == 'divide':
            res = requests.get("http://div-service:5054/{}/{}".format(number_1,number_2)).json()
        
        elif operation == 'equal':
            res = requests.get("http://equal-service:5057/{}/{}".format(number_1,number_2)).json()
            
        elif operation == 'exponent':
            res = requests.get("http://exponent-service:5056/{}/{}".format(number_1,number_2)).json()
            
        elif operation == 'modulus':
            res = requests.get("http://modulus-service:5055/{}/{}".format(number_1,number_2)).json()
            
        
        result = res["ans"]
        flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="landing-service"
    )
    