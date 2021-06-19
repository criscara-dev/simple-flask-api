from flask import Flask, request
from flask_restful import Resource, Api
from secure_check import authenticate,identity
from flask_jwt import JWT ,jwt_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
api = Api(app)

jwt = JWT(app, authenticate, identity)      

avengers = []

class Avengers(Resource):
    def get(self,name):
        # print(avengers)
        # Iterate through list for avengers
        for avenger in avengers:
            if avenger['name'] == name:
                return avenger

        # If you request a avenger not yet in the avengers list
        return {'name':None},404

    def post(self,name):
        # create a dictionary
        avenger = {'name':name}
        # Add the dictionary to list
        avengers.append(avenger)
        # print(avengers)
        # Then return it back
        return avenger

    def delete(self,name):
        # Iterate through list for avengers
        for index,avenger in enumerate(avengers):
            if avenger['name'] == name:
                delted_avenger = avengers.pop(index)
                return {'note':'delete successful'}


class AllNames(Resource):
    @jwt_required()
    def get(self):
        # return all the avengers
        return {'avengers': avengers}


api.add_resource(Avengers, '/avenger/<string:name>')
api.add_resource(AllNames,'/avengers')

if __name__ == '__main__':
    app.run(debug=True)
