
from flask import Flask
from flask_restful import Api, Resource

import requests
import os

app = Flask(__name__)
api = Api(app)
app.secret_key = 'thisisjustarandomstring'


class Multiplication(Resource):
        
    def get(self,num1,num2):
        return {"ans":num1*num2}
    
api.add_resource(Multiplication, "/<int:num1>/<int:num2>")

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5053,
        host="mul-service"
    )


