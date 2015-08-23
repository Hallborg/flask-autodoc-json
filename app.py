from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from flask.ext.autodoc import Autodoc

import requests
import autodoc_json
app = Flask(__name__)
auto = Autodoc(app)

# @app.route(arg) creates a path to the specified arg
# @auto.doc() takes the route and function where it's located and
# creates an object of it for the documentation


@app.route('/docs')
@auto.doc()
def doc_html():
    '''sends the auto generated documentation page'''
    return auto.html()


@app.route('/docs/json')
@auto.doc()
def doc_json():
    '''sends the auto generated documentation in JSON'''
    data = autodoc_json.generate_json(auto.generate())
    # response.data.items=data, response.status_code = 200
    # for more information on make_response:
    # http://flask.pocoo.org/docs/0.10/api/
    response = make_response(
        jsonify(items=data),
        200
    )
    return response


@app.route('/user/<int:id>', methods=['GET'])
@auto.doc()
def show_user(id):
    '''Example on RESTful endpoint - show user by id'''
    # returning only the jsonified object work fine, but it will set the
    # status_code to 200 at all times
    # example on returning values 1-3
    if id is 1:
        return 'hello' + str(id)
    elif id is 2:
        return jsonify({'msg': 'hello', 'id': id})
    elif id is 3:
        resp = make_response(jsonify({'msg': 'hello', 'id': id}), 200)
        # status is created from the status_code (second arg in make_response)
        print resp.status
        return resp


@app.route('/user/<int:id>', methods=['DELETE'])
@auto.doc()
def delete_user(id):
    '''Example on RESTful endpoint - delete user by id'''
    # notice how the uri for this function is the same as show_user
    return 'Deleted user ' + str(id)


@app.route('/user', methods=['POST'])
@auto.doc()
def create_user():
    '''create a new user'''
    # posting to an endpoint is often different from a http get
    # Since post data mostly contains more than one value to create an
    # object, in this example a user.

    # a post uri similar to the 'GET' above could look something like this:
    # '/user/<string:first_name>/<string:last_name>/<string:gender>/<int:age>'
    # and that is just to complicated to use
    # thats why we use the requsts own body to store data (like a form does
    # in html)

    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    gender = request.form.get('gender')
    age = request.form.get('age')

    # create user(first_name, last_name, gender, age)
    return make_response('User created', 201)


if __name__ == '__main__':
    app.run(debug=True)
