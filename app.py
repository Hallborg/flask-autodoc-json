from flask import Flask
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
    response = make_response(
        jsonify(
            data=autodoc_json.generate_json(auto.generate())),
            200
    )
    return response


@app.route('/user/<int:id>')
@auto.doc()
def show_user(id):
    return 'hello' + str(id)


if __name__ == '__main__':
    app.run(debug=True)
