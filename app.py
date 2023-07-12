

from markupsafe import escape
from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index/')
def hello():
    return'<h1>Hello world!</h1> '
# http://127.0.0.1:5000/index

@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'

# TO AVOID CROSS SITE SCRIPTING
@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))
# http://127.0.0.1:5000/capitalize/hello

@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)
# http://127.0.0.1:5000/add/5/5/

@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    return '<h2>Hi {}</h2>'.format(users[user_id])
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)
        
# http://127.0.0.1:5000/users/0
# the one for an app with identification
