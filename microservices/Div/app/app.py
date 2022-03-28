
from flask import Flask
from flask_restful import Api, Resource

import requests
import os

app = Flask(__name__)
api = Api(app)
app.secret_key = 'thisisjustarandomstring'


class Division(Resource):
        
    def get(self,num1,num2):
        if(num2==0):
            return {"ans":"Math Error"}
        return {"ans":num1/num2}
    
api.add_resource(Division, "/<int:num1>/<int:num2>")

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5054,
        host="div-service"
    )


