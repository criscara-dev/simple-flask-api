# SIMPLE RESTful API

## Why we need REST?

We can visit a website manually but there are cases we want to access it programmatically, basically let a server access our Database;
Here it come the Representation State Transfer.
REST is a standard way for computer to communicate over the web. If our system follow those rules is also knows as _RESTful_.
It allows full interaction and operation between computer systems online.

ex.
So, let's imagine now we are a Market Exchange (that let trade Stocks, ETFs, Cryptos etc. ) and we want our client to access our system directly (automatically/programmatically) to buy/sell.
We can now implementing a REST API.

## REST verbs

[REST verbs](https://restfulapi.net/http-methods/)

| Action | RESTterm |
| ------ | -------- |
| Create | POST     |
| Read   | GET      |
| Update | PUT      |
| Delete | DELETE   |
| ...    | ...      |

## POSTMAN

There are different tools that let us test our REST API endpoints; from our Terminal ( CLI tools ) or using a program such as [Postman](https://www.postman.com/).
We will be using Postman.
The common way to send payload information back in REST is the JSON format; a key, values pair format similar to a Python dictionary.

## Flask-RESTful Library

[Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
We just need this module in order to communicate with our back-end to implement a RESTful API

## Our API with basic CRUD operations

```python
class Avengers(Resource):
    def get(self,name):
        pass

    def post(self,name):
        pass

    def delete(self,name):
       pass


class AllNames(Resource):
    pass
```

## Implementing Authorization

We are using the library [Flask JWT](https://pythonhosted.org/Flask-JWT/) to add a layer of security to our REST API to be able to view all the _avengers_ in the dictionary.
As from the code below, this is only for the endpoint `api.add_resource(AllNames,'/avengers')`, thank to the usage of the `@jwt_required()` **decorator**.
All the other CRUD operations are available without restrictions.

```python
# ...
class AllNames(Resource):
    @jwt_required()
    def get(self):
        # return all the avengers
        return {'avengers': avengers}


api.add_resource(Avengers, '/avenger/<string:name>')
api.add_resource(AllNames,'/avengers')
```

We need now to create a new _class_ User, to be able to authorize some users, and the module to import the 2 methods we need to authenticate and verify the identity of users we create.

At this time the endpoint `/avengers` is not available:
![Endpoint not yet available](./static/need-token.png)

## POSTMAN endpoints testing

Flask-JWT has already create the endpoint for us: [http://127.0.0.1:5000/auth](http://127.0.0.1:5000/auth).

Here we need to set:

| Where        | What             |
| ------------ | ---------------- |
| HEADERS      | KEY/VALUES       |
| Content:Type | application/json |

and now we need to:

1. pass username and password as json, as specified
2. submit the POST request
3. grab the generated token and pass it as:

| Where         | What           |
| ------------- | -------------- |
| HEADERS       | KEY/VALUES     |
| Authorization | JWT token-here |

![grab access token](./static/grab-access-token.png)
![Passing token](./static/passing-token.png)

Finally the endpoint is authorized and we can access the data.

![Endpoint payload token](./static/endpoint-payload.png)
