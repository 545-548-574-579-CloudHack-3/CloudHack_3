from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import Api, Resource

import requests
import os

app = Flask(__name__)
api = Api(app)
app.secret_key = 'thisisjustarandomstring'

@app.route('/', methods=['POST', 'GET'])
def index():
    if(request.form!={}):
        number_1 = float(request.form.get("first"))
        number_2 = float(request.form.get('second'))
        operation = request.form.get('operation')
        result = 0
        if operation == 'add':
            result = add(number_1, number_2)
        elif operation == 'minus':
            result =  minus(number_1, number_2)
        elif operation == 'multiply':
            result = multiply(number_1, number_2)
        elif operation == 'divide':
            result = divide(number_1, number_2)

        flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
    
"""
api.add_resource(Addition, "/add/<int:num1>/<int:num2>")
api.add_resource(Subtraction, "/sub/<int:num1>/<int:num2>")
api.add_resource(Multiplication, "/mul/<int:num1>/<int:num2>")
api.add_resource(Division, "/div/<int:num1>/<int:num2>")

class Addition(Resource):

    def get(self,num1):
        pass

    def post(self):
        pass
        
"""