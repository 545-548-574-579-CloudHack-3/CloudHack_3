
from flask import Flask
from flask_restful import Api, Resource

import requests
import os

app = Flask(__name__)
api = Api(app)
app.secret_key = 'thisisjustarandomstring'


class Equal(Resource):
        
    def get(self,num1,num2):
        if num1==num2:
            return {"ans":"True"}
        return {"ans":"False"}
        
api.add_resource(Equal, "/<int:num1>/<int:num2>")

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5057,
        host="equal-service"
    )


