from flask import Flask
from flask import url_for
from flask import request
from flask import render_template

from markupsafe import escape


"""
To just run:
    $ export FLASK_APP=${FILE_NAME}
    $ flask run
"""

app = Flask(__name__)

@app.route("/hello_world")
def hello_world():
    """
    route() decorator is the fuction where url trigger
    """
    return "<p>Hello, World!</p>"


@app.route("/<name>")
def hello(name):
    """
    escape() can protect from injection attacks.
    
    And I don't have like he route, so it will not return 404, just `Hello, he!`
    """
    return f"Hello, {escape(name)}!"

@app.route("/")
def index():
    return "Index Page"

@app.route("/hello")
def Hello():
    return "Hello, World"


"""
Variable Rules: `<converter:variable_name>`
"""
@app.route('/user/<username>')
def profile(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'


"""
Unique URLS/ Redirection Behavior
"""
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/register')
def register():
    return 'register'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('register'))
    print(url_for('register', next='/'))
    print(url_for('profile', username="John Doe"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    By default, a route only answers to `GET` requests.
    """
    if request.method == "POST":
        return do_the_login()
    else:
        return show_the_login_form()

def do_the_login():
    return 'do_the_login'

def show_the_login_form():
    return 'show_the_login_form'

# to generate URLs for static file, where in `static/style.css`
# url_for('static', filename='style.css')

# @app.route('/welcome/')
# @app.route('/welcome/<name>')
# def welcome(name=None):
#     return render_template('weilcome.html', name=name)


if __name__ == '__main__':
    app.run()
