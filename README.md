# flask-autodoc-seed

Flask is a great tool for running web servers and has a lot of add-ons and functionallity from pypi and github.

Getting started with flask applications is not hard but finding all the good stuff around it
might be tricky for beginners (like myself). I've been looking into flask and have now created a small
seed application with some of the good stuffs of pypi. 

### Packages 
* Flask (Main package)
* jsonify (Converting data to be accessed via the API)
* make_response (HTTP response with easy modifiable status code)
* render_template (Easy way to show html docs)
* requests (HTTP for humans, simple way to do HTTP requests)
* Autodoc (Used for docing API)
* autodoc_json (converts the doc:ed api to json)

## Getting started

After cloning the repository you'll have to path to the folder
and install the dependencies.

``pip install -r requirements.txt``

And to start the application

``python app.py``

Open a browser and go to http://localhost:5000
Look in app.py to find out more. Keep what you need and reform app.py so it fits your solution! 
